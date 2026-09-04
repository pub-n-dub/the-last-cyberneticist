# Episode 13 Script

## Title

`A Truly Machine-Intelligent System: The Autonomous Board`

## Script

Welcome to Episode 13 of `The Last Cyberneticist`.

This episode is called `A Truly Machine-Intelligent System: The Autonomous Board`.

Episode 9 argued that architecture can be understood as a language in matter. This episode asks the practical follow-up: what happens when the relation shown by the comparator is allowed to enter a controlled cycle?

The answer is not to keep adding parts to the photographed Four-Bit Wonder until its original clarity disappears. That board remains intact. It is the manual reference machine: small, readable, and useful precisely because a person remains inside every operation.

The autonomous version is a separate build on a new Vector `8016-1` wire-wrap board.

Its first job is deliberately narrow. Capture a four-bit target. Read one candidate word from SRAM. Compare candidate and target. If the candidate is too low, raise it by one step. If it is too high, lower it by one step. Write the revised word back. Stop when the candidate and target match.

That is a hill climber.

It is not a general intelligence. It is not a machine with a hidden interior life. It is a controlled read-compare-step-write cycle whose behavior can be watched at a slow clock rate.

The distinction matters because the whole value of this project lies in keeping the claim proportional to the evidence. The target latch holds the desired word. The candidate register holds the value under revision. The `74LS85` produces the relation. The sequencer gives each operation a place in time. A tri-state driver makes sure that the revised value is placed on the SRAM bus only when it is safe to write.

In other words, the machine has to earn every step.

Read and load.

Compare.

Step.

Write.

Then begin again, unless equality has halted the cycle.

The build order should follow the same logic. First verify the mode controls. Then verify the comparator indications. Then capture a target and prove that it remains stable. Then make one controlled up or down step without writing SRAM. Then test one automatic read-modify-write cycle. Only after that should continuous operation be allowed.

This is not caution for its own sake. It is how we prevent bus contention, accidental writes, and a story that outruns the machine.

Phase 1 concerns a single selected address. Phase 2 extends the idea across the exposed sixty-four addresses. An automatic address counter moves on only after the current location reaches its target. The board therefore becomes a small field of local corrections rather than a single demonstration.

There is an optional future extension in which each address has its own stored target. That is interesting, but it is not necessary for the first achievement. The first achievement is enough: the board sees a difference, acts once in the indicated direction, preserves the result, and stops when the relation is satisfied.

The difference is no longer only displayed.

It has entered the machine's own cycle of correction.

