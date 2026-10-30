# Episode 15 Audioplay Plan

## Principle

The storyboard carries the argument; the audioplay gives it dramatic pressure,
space, and rhythm. Character voices are original performances, not imitations of
real people. Historical figures may be represented through attributed document
readings or clearly labeled reconstructions.

Every recorded line must be assigned one of these statuses in the session log:

- `NARRATION` — present-day host's argument.
- `DOCUMENT READING` — verified quotation, with source identifier.
- `RECONSTRUCTION` — invented but historically plausible dialogue or action.
- `SOUND ONLY` — a nonverbal scene or transition.

## Cast and voice direction

| Voice | Dramatic role | Performance direction | Permitted material |
| --- | --- | --- | --- |
| Host | Investigator and guide | Close, natural, precise; curiosity held in check by doubt. | Narration; transitions; stated inferences. |
| Archivist | Fictional evidentiary counterweight | Clear, measured, dry warmth; slightly more distant mic position. | Source framing; challenges; reads citations. |
| Document Reader: Berkeley | Gives the historical record a human presence | Original neutral period-inflected reading; no mimicry. | Verified Berkeley text only, attributed on screen. |
| Document Reader: Koff | Makes hands-on Squee work tangible | Practical, unshowy original reading; no mimicry. | Verified Koff text only, attributed on screen. |
| Workshop Voice A | Mechanical/fabrication perspective | Restrained, work-focused; distinguish through pace, not effects. | Reconstruction only. |
| Workshop Voice B | Electrical/integration perspective | Thoughtful, terse; natural voice. | Reconstruction only. |
| Tati Robot | Recurring nonverbal presence | Electromechanical motif, not a speech synthesizer. | Sound only. |

Do not give Porter, Jensen, Vall, Dennett, Berkeley, or Koff invented dialogue
under their own names. Where a reconstruction needs human speech, identify it as
an unnamed workshop voice in both the storyboard and session log.

## Recording method

Record each spoken part dry, mono, 48 kHz/24-bit WAV. Preserve:

1. original take;
2. selected edit;
3. processed mix stem; and
4. final mix reference.

Character separation should come first from writing, pacing, mic distance, and
room treatment. Use processing sparingly: gentle EQ and dynamics for clarity;
subtle room for Archivist/document readings; no synthetic impersonation or
voice clone. Test each treatment on headphones and a phone speaker.

## Sound-byte library

Build short, clean, reusable sounds rather than one long atmospheric recording.
Each asset gets an ID, source/recording note, duration, rights status, and
recommended loudness.

| ID range | Sound bytes | Use |
| --- | --- | --- |
| `ARC-01`–`ARC-08` | paper sleeve, photograph set down, page turn, pencil, desk lamp, filing drawer, room tone, chair movement | Archive and evidence-card transitions. |
| `DOC-01`–`DOC-05` | typewriter key cluster, paper feed, stamp, binder close, microfilm/projector-style mechanical texture | Published-line and document moments; use lightly. |
| `WRK-01`–`WRK-12` | screw tray, screwdriver, wire handling, chassis tap, relay click, switch throw, soldering ambience, motor test, fan/ventilation, tool set-down | Explicitly reconstructed workshop scenes. |
| `TATI-01`–`TATI-06` | contact click, low motor strain, spring movement, head/jaw-like mechanism, stalled motion, silence tail | The robot motif: click → strain → motion → stop. |
| `TRN-01`–`TRN-04` | low tonal bridge, tape-stop-like restraint, short room decay, single piano/harmonium note if licensed or recorded | Section changes only; never cue a false revelation. |

Record original Foley where possible. Do not lift historical recordings, film
audio, commercial effects, or music without a documented licence. A sound made
for a reconstruction must not be presented as recorded evidence of the original
robot.

## Board-to-audio handoff

For each storyboard board, add these fields:

| Field | Requirement |
| --- | --- |
| `Voice` | Host, Archivist, Document Reader, Workshop A/B, or none. |
| `Line status` | Narration, Document Reading, Reconstruction, or Sound Only. |
| `Audio assets` | Exact IDs, not a vague instruction such as “workshop sounds.” |
| `Mix intent` | Foreground, under narration, transition, or silence. |
| `Evidence check` | Required for every documentary reading and on-screen quote. |

Silence is an intentional asset. It should follow an unresolved source gap and
precede the final `BUILDER: UNKNOWN` return.

## First recording package

Prepare a 2½-minute proof-of-format for storyboard boards 01–06:

1. Host cold open and evidence contract.
2. Archivist correction: provenance is not authorship.
3. `ARC-01`, `ARC-02`, and `ARC-07` archive Foley.
4. `TATI-01` through `TATI-06` as the robot motif.
5. A 10–15 second stretch of deliberate silence after the empty maker field.

Approve this proof only when voices remain distinct without heavy processing,
the evidence labels are intelligible, and the Tati motif feels particular rather
than generic.
