# Episode 14 Script

## Title

`The Preessence Esoteric of Motorola`

## Script

Welcome to Episode 14 of `The Last Cyberneticist`.

This episode is called `The Preessence Esoteric of Motorola`.

We have spent time with wires, memory, comparators, and the small visible cycles that make a machine seem to act. But there is another object at the center of all of this: the processor.

The processor is not the whole computer. It cannot remember without memory, speak without an interface, or persist without ROM. But it is where instruction, timing, address, and decision are gathered into a sequence.

For this part of the story, the Motorola `6808` and `6809` matter because they make that sequence legible.

They belong to an era when a computer's boundaries could still be held in view. Registers have names. Buses have jobs. An instruction reaches for an address. A peripheral occupies a place in memory. A reset vector tells the processor where to begin.

None of that is mystical.

It is an agreement between silicon, wiring, and program.

The M6x09-II-SBC gives us a concrete way to see the agreement. Its `6809` does not float in an invisible cloud of services. It reads from memory, reaches the serial interface, and begins in ROM. What software can do depends on those physical arrangements: how memory is divided, what address belongs to a device, what clock is available, and what instructions the processor understands.

This is why processor choice is never merely a matter of speed or nostalgia.

Choose a processor and you also choose a vocabulary of operations, a shape of memory, a set of constraints, and a particular discipline for the programmer. The machine does not become less expressive because its limits are visible. Its limits become possible to reason about.

That is the useful contrast with contemporary computing. We are often asked to accept an enormous system without being able to locate its boundaries. Here, we can point to the processor, the ROM, the RAM, the serial path, and the program that crosses between them.

The point is not that the `6809` is secretly more intelligent than a modern processor.

The point is that it is close enough to the bench that we can ask better questions.

What does this instruction change?

Where does this value live?

What happens after reset?

And how do we know that the program we wrote is the program the machine will actually execute?

That final question takes us from the processor to the chip that holds its first instructions.

Next time, we burn the ROM.
