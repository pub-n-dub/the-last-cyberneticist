# Episode 10: ASSIST09 ROM Workflow Shadow

This companion record grounds Episode 10, `Away from scratch-building toward manufactured production`, in the M6x09-II-SBC workflow it describes.

## What The Episode Claims

The episode argues that a finished board becomes reproducible when its software path can be rebuilt, checked, loaded, tested, and preserved without relying on one person's memory.

The corresponding technical record is [ASSIST09 Baseline Output Record](../../../../cartheur/M6x09-II-SBC/roms/assist09-baseline-output-2026-09-04.md).

## Evidence Available Now

- ASSIST09 rebuilds deterministically to a 2,048-byte image mapped at `$F800-$FFFF`.
- The generated image matches the checked-in baseline byte for byte.
- Its reset vector is `$F837`.
- A separate S-record smoke test is built for RAM address `$1000` and prints `ASSIST09 RAM SMOKE TEST PASSED` when run through the monitor.

## Evidence Still Required

The physical proof remains intentionally open:

1. Program the verified image into an EPROM with the Batronix Barlino II 32P and complete readback verification.
2. Reset the M6x09-II-SBC and capture the ASSIST09 terminal prompt.
3. Load the RAM smoke-test S-record through the terminal and run `G 1000`.
4. Record the success message and returned prompt for the specific board, EPROM, serial adapter, and terminal settings.

This distinction matters to the episode. Reproducibility is not a claim that a source file exists. It is a chain of evidence that survives the trip from source text to the behavior of a particular machine.
