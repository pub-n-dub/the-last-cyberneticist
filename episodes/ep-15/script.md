# Episode 15 Script

## Title

`Feel the (ROM) Burn`

## Script

Welcome to Episode 15 of `The Last Cyberneticist`.

This episode is called `Feel the (ROM) Burn`.

In the previous episode, we followed the processor to its first question after power-on: where do I begin?

For the M6x09-II-SBC, the answer is an EPROM.

The `27C128` does not contain an idea of a program. It contains the actual bytes that the processor will read when the board resets. If those bytes are wrong, the machine's behavior is wrong. If we cannot say where they came from, how they were built, or whether they were verified, then we do not yet have a durable system. We have a guess installed in a socket.

That is why ROM burning deserves to be treated as software work in material form.

The reliable path begins before the programmer is switched on. Build the ASSIST09 monitor from source. Verify the resulting ROM image. Use the known-good monitor to load an experiment into RAM through the serial terminal. Run it there first.

RAM is the fast loop.

It is where a program can be changed, sent, tested, and changed again without turning every small experiment into a permanent hardware operation.

Only when the image has earned trust in RAM should it become an EPROM candidate.

Then the task becomes careful and ordinary. Read the existing chip and preserve a backup. Select the exact device. Blank-check the replacement. Program the verified image with the Batronix Barlino II 32P. Verify the result. Label the chip with its image and date. Record what board, adapter, and test conditions were involved.

Each step is modest.

Together, they turn a file into a milestone.

The value is not in the drama of putting a chip into a programmer. The value is that a later person can recover the chain of evidence: this source made this image; this image passed this test; this chip contains that image; this board booted with it.

That is how behavior becomes durable without becoming mysterious.

A burned ROM is not the end of experimentation. It is the point at which one experiment is stable enough to support the next.
