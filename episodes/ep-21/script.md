# Episode 21: Little-Lost Robot: Initial Preparations

## Script

Welcome to Episode 21 of *The Last Cyberneticist*.

Before a machine can teach us anything, we have to reduce the number of ways our own preparation can mislead us.

That sounds less dramatic than a robot moving for the first time. It is also what makes that first movement interpretable.

This episode begins the preparation cycle for the Little-Lost Robot work. The aim is not to collect equipment for its own sake. The aim is to establish a few reusable, known conditions before we begin asking a more complicated machine to behave.

The first condition is power.

A USB power source is convenient because it is common, replaceable, and easy to test. But a connector is not yet a bench tool. The useful object is a simple cable made from a USB-A lead, with the power lines identified, insulated, and terminated in square-pin female jumpers that can meet a prototype safely.

The Boagaphish Four-Bit Wonder is a good place to illustrate the method. It is small enough that we can see what power enters, what changes when it is present, and what should remain stable. Before the cable meets the robot, it should meet a system whose expected behavior is already understood.

That is a general rule for preparation: test a new tool against a known machine before using it to interpret an unknown one.

The second condition is programmable memory.

Old and new programming tools each have a place. A modern device may be faster, easier to verify, and better supported. An older ROM burner may match the physical parts and workflow of the machines we are trying to understand. The choice should not be made for nostalgia or novelty. It should be made by asking which device supports the exact memory, which image can be verified, and which process can be repeated.

Restoring a straightforward ROM burner is part of that discipline. The restoration is not complete when the machine powers on. It is complete when the burner can identify the intended device, read a known chip, perform a blank check when appropriate, program a test image, verify it against the source file, and leave a record of the result.

That record matters because a programmed chip is otherwise a sealed assertion. If we do not know what image went in, when it was made, how it was checked, and which device received it, a later failure becomes harder to distinguish from every other possible failure.

The cable and the programmer may look like separate chores. They are not. Both reduce uncertainty at the boundary between an intention and a physical machine. One makes power available in a controlled way. The other makes instructions persistent in a controlled way.

Neither should be heroic. The goal is to make the ordinary dependable.

In the next episode, these preparations come together: stable power, known-good memory, a clearer view of the processor and support hardware, and a bench procedure that makes the first live trials safer to read.

Thank you for listening.

## Drafting note (not spoken)

Before recording, verify the USB cable polarity and voltage with a multimeter, identify the actual programmer and supported devices, and show only restoration steps that have been completed safely.
