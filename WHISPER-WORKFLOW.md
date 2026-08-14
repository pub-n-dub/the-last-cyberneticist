# Whisper Workflow

Recovered on Wednesday, August 12, 2026 while transcribing Episode 3.

## Source audio

- [published/episode-03.mp3](/home/cartheur/ame/aiventure/aiventure-github/dublications/the-last-cyberneticist/episodes/ep-03/published/episode-03.mp3:1)
- [project/episode-3.aup3](/home/cartheur/ame/aiventure/aiventure-github/dublications/the-last-cyberneticist/episodes/ep-03/project/episode-3.aup3:1)

## Recovered model paths

These models were already downloaded outside this repo in the local `whisper.cpp` fork:

- `/home/cartheur/ame/aiventure/aiventure-github/forks/whisper.cpp/models/ggml-base.en.bin`
- `/home/cartheur/ame/aiventure/aiventure-github/forks/whisper.cpp/models/ggml-tiny.en.bin`

Shell history entries that recovered this:

- `git clone https://github.com/cartheur-forks/whisper.cpp.git`
- `wget -O /home/cartheur/ame/aiventure/aiventure-github/forks/whisper.cpp/models/ggml-tiny.en.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.en.bin`
- `wget -O /home/cartheur/ame/aiventure/aiventure-github/forks/whisper.cpp/models/ggml-base.en.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.en.bin`

## Local build used

The fork checkout was present but not built. A clean local build was created in `/tmp`:

- source copy: `/tmp/whisper-src`
- build dir: `/tmp/whisper-build`
- executable: `/tmp/whisper-build/bin/whisper-cli`

Build command used:

```bash
cp -a /home/cartheur/ame/aiventure/aiventure-github/forks/whisper.cpp /tmp/whisper-src
cmake -S /tmp/whisper-src -B /tmp/whisper-build -DCMAKE_BUILD_TYPE=Release -DWHISPER_COMMON_FFMPEG=ON
cmake --build /tmp/whisper-build -j4
```

The direct build from the fork checkout failed because the standalone CMake config tries to write `bindings/javascript/package.json` back into the source tree.

## Episode 3 transcription command

```bash
mkdir -p episodes/ep-03/transcripts
/tmp/whisper-build/bin/whisper-cli \
  -m /home/cartheur/ame/aiventure/aiventure-github/forks/whisper.cpp/models/ggml-base.en.bin \
  -f episodes/ep-03/published/episode-03.mp3 \
  -otxt \
  -of episodes/ep-03/transcripts/episode-03
```

## Output

- [transcripts/episode-03.txt](/home/cartheur/ame/aiventure/aiventure-github/dublications/the-last-cyberneticist/episodes/ep-03/transcripts/episode-03.txt:1)

## Notes

- The transcription is a raw `whisper.cpp` pass, not a polished script.
- Proper nouns need cleanup. Current obvious misses include `Wiener`, `Grey Walter`, and `Heiserman`.
- The pass took about `102.6` seconds wall-clock according to `whisper.cpp` timings.
