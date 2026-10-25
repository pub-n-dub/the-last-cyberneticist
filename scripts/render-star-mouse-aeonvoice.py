#!/usr/bin/env python3
"""Render Fredric Brown's *The Star Mouse* with the local AeonVoice engine."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "readings" / "The Star Mouse - Fredric Brown.txt"
CLEAN_TEXT = REPO / "readings" / "The Star Mouse - Fredric Brown.aeonvoice.txt"
OUTPUT = REPO / "readings" / "The Star Mouse - AeonVoice.mp3"
VOICE_ROOT = REPO.parents[1] / "voice" / "aeon-voice"
ENGINE = VOICE_ROOT / "build" / "linux" / "test" / "AeonVoice-test"

VOICES = {
    # Profile, rate, pitch, volume.  Values are percentages of AeonVoice's
    # neutral settings: subtle contrast keeps the reading intelligible.
    "narrator": ("Bdl", 88, 96, 100),
    "mitkey": ("Toptygin", 96, 106, 100),
    "professor": ("Evgeniy-Eng", 86, 94, 98),
    "klarloth": ("Ksp", 84, 92, 98),
    "bemj": ("Helen", 94, 102, 100),
}


def clean_source(raw: str) -> str:
    """Remove scan furniture and the unrelated magazine feature after the story."""
    raw = raw.split("By FREDRIC BROWN", 1)[-1]
    raw = re.split(r"(?m)^PS.d feature", raw, maxsplit=1)[0]
    lines: list[str] = []
    in_illustration = False
    for line in raw.splitlines():
        stripped = line.strip()
        if stripped == "NOT OER":
            in_illustration = True
        if in_illustration:
            if "WO Busr" in stripped:
                in_illustration = False
            continue
        if (
            not stripped
            or re.fullmatch(r"\[Printed page \d+\]", stripped)
            or re.fullmatch(r"\d+(?:\s+PLANET)?", stripped)
            or re.fullmatch(r"(?:THE STAR[-^A-Z]+|STORIES|STOMUES)", stripped)
            or stripped == "Illustrated by Lynch"
            or re.fullmatch(r"[IVX]+", stripped)
        ):
            lines.append("")
            continue
        lines.append(line)

    text = "\n".join(lines)
    text = re.sub(r"-\n", "", text)  # Repair printed-line hyphenation.
    text = re.sub(r"\n[ \t]*\n+", "\n\n", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n\n *", "\n\n", text)
    text = text.replace("T hat", "That").replace("MItkey", "Mitkey")
    text = text.replace("an)rthing", "anything").replace("vvoozy", "woozy")
    return text.strip() + "\n"


def explicit_voice(context: str, quote: str, phase: str) -> str | None:
    """Choose a voice for a quoted turn when its attribution is visible nearby."""
    nearby = context.lower()
    words = quote.lower()
    patterns = {
        "klarloth": r"\b(klarloth)\b",
        "bemj": r"\b(bemj)\b",
        "professor": r"\b(professor|oberburger)\b",
        "mitkey": r"\b(mitkey)\b",
    }
    for role in ("klarloth", "bemj", "professor", "mitkey"):
        name = patterns[role]
        if re.search(rf"{name}.{{0,45}}\b(said|asked|told|called|interrupted|again|replied)\b", nearby):
            return role
        if re.search(rf"\b(said|asked|told|called|interrupted)\b.{{0,45}}{name}", nearby):
            return role
        if re.search(rf"{name}\s*:", context, re.I):
            return role

    # Reliable in-character address cues in unattributed exchanges.
    if "brofessor" in words or "herr klarloth" in words or "herr bemj" in words:
        return "mitkey"
    if "mitkey" in words and phase == "earth":
        return "professor"
    if "klarloth" in words:
        return "bemj"
    if "bemj" in words:
        return "klarloth"
    return None


def make_segments(text: str) -> list[tuple[str, str]]:
    segments: list[tuple[str, str]] = []
    last_voice = "professor"
    phase = "earth"
    quote_re = re.compile(r"([“\"][^”\"]+[”\"])")

    for paragraph in re.split(r"\n\n+", text):
        if not paragraph.strip():
            continue
        if "Prxl is an asteroid" in paragraph or "P RXL is an asteroid" in paragraph:
            phase = "prxl"
        pos = 0
        for match in quote_re.finditer(paragraph):
            narration = paragraph[pos : match.start()].strip()
            if narration:
                segments.append(("narrator", narration))
            quote = match.group(1)
            context = paragraph[max(0, match.start() - 100) : min(len(paragraph), match.end() + 140)]
            role = explicit_voice(context, quote, phase)
            if role is None:
                role = last_voice if phase == "prxl" else "professor"
            last_voice = role
            segments.append((role, quote))
            pos = match.end()
        tail = paragraph[pos:].strip()
        if tail:
            segments.append(("narrator", tail))

    # Combine adjacent same-voice fragments; fewer engine invocations preserve cadence.
    merged: list[tuple[str, str]] = []
    for role, text_part in segments:
        text_part = re.sub(r"\s+", " ", text_part).strip()
        if not text_part:
            continue
        if merged and merged[-1][0] == role:
            merged[-1] = (role, merged[-1][1] + " " + text_part)
        else:
            merged.append((role, text_part))
    return merged


def run(command: list[str], **kwargs: object) -> None:
    subprocess.run(command, check=True, **kwargs)


def main() -> int:
    if not ENGINE.is_file():
        raise FileNotFoundError(f"AeonVoice engine not found: {ENGINE}")
    if shutil.which("ffmpeg") is None:
        raise FileNotFoundError("ffmpeg is required to assemble the final MP3.")

    cleaned = clean_source(SOURCE.read_text(encoding="utf-8"))
    CLEAN_TEXT.write_text(cleaned, encoding="utf-8")
    segments = make_segments(cleaned)
    if not segments:
        raise RuntimeError("No narratable text was found.")

    work = Path("/tmp/star-mouse-aeonvoice")
    if work.exists():
        shutil.rmtree(work)
    work.mkdir()
    env = {
        "AEONVOICE_DATA_PATH": str(VOICE_ROOT / "data"),
        "LD_LIBRARY_PATH": ":".join(
            str(path)
            for path in (
                VOICE_ROOT / "build" / "linux" / "core",
                VOICE_ROOT / "build" / "linux" / "audio",
                VOICE_ROOT / "build" / "linux" / "lib",
            )
        ),
    }

    wavs: list[Path] = []
    for index, (role, words) in enumerate(segments, start=1):
        wav = work / f"{index:04d}-{role}.wav"
        print(f"[{index}/{len(segments)}] {role}: {words[:72]}", flush=True)
        profile, rate, pitch, volume = VOICES[role]
        run([
            str(ENGINE), "-p", profile, "-r", str(rate), "-t", str(pitch),
            "-v", str(volume), "-q", "max", "-o", str(wav),
        ], input=words + "\n", text=True, env=env)
        wavs.append(wav)

    concat = work / "concat.txt"
    concat.write_text("".join(f"file '{wav}'\n" for wav in wavs), encoding="utf-8")
    master = work / "master.wav"
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(master)])
    run([
        "ffmpeg", "-y", "-v", "error", "-i", str(master), "-af", "loudnorm=I=-18:TP=-2:LRA=7",
        "-ac", "1", "-ar", "24000", "-c:a", "libmp3lame", "-b:a", "64k", str(OUTPUT),
    ])
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
