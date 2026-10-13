# Episode 13: Feel the (ROM) Burn

## Script

Episode 12 established that a machine can know its next move only when its state, permitted actions, and record of conduct are explicit.

But a controller cannot act on a program that exists only in our notes or on a modern host. Before the next experiment can be loaded, tested, and repeated, this board needs a dependable place to begin after power-up: a monitor in ROM, a serial path that actually works, and evidence that the bytes we intended are the bytes the processor will execute.

That is where we turn now—from the logic of a lawful next move to the material question of how a machine receives its first instructions.

Welcome to Episode 13 of *The Last Cyberneticist*.

This episode is called *Feel the (ROM) Burn*.

There is a familiar little drama in old-computer work. A chip is placed in a programmer. A progress bar crosses a screen. The chip is removed, labelled, and pressed into a socket. Then, if all goes well, a machine that had been silent presents a prompt.

It is tempting to make that the story: the old ritual, the satisfying click of a socketed EPROM, the moment a program becomes a physical object.

But that moment is only the visible end of a longer chain. A ROM programmer is exceptionally literal. It does not know whether an image was assembled from the intended source, whether it ends at the intended address, whether its reset vector points to executable code, or whether a serial interface has been configured so that its own flow-control signal prevents it from speaking. It accepts bytes, places bytes in a chip, and leaves the rest to us.

So the real question in this episode is not simply how to burn a ROM. It is this: when can a program placed in ROM be called a dependable beginning for a machine?

For the M6x09-II single-board computer, the answer turned out to be larger than one successful burn. It required a monitor rebuilt from its original source, an image whose fixed layout was checked, a serial interface whose register contract was corrected, measurements on the physical board, a full EPROM readback, and a terminal that behaved as part of the protocol rather than as an innocent window onto it.

At the end of that work, the result looked almost disappointingly simple:

`ASSIST09 RAM SMOKE TEST PASSED`

Then:

`ASSIST09`

And a prompt.

Those lines are not much to look at. But they mean that a board without a CTS jumper now boots at 115200 baud, receives a small program through its serial port, writes it into RAM, executes it, returns to the monitor, and remains ready for the next experiment. The point is not that the prompt is spectacular. The point is that it is earned.

The program at the centre of this work is ASSIST09, a monitor for the Motorola 6809. A monitor is a small recovery environment. It lives at a known address, comes up after reset, talks over a serial line, and gives a human operator a narrow but immensely useful foothold: inspect memory, load a program, begin execution, and return when the experiment is done.

That makes it a very good object for this series. The monitor is not intelligence in any grand sense. It is a way of refusing to begin from nothing each time. It gives the machine a stable first conversation.

There was an immediate practical difficulty. The project included an assembler executable from 2004, but that executable would not run on the present host. There are easy ways to conceal such a problem. One could obtain an opaque replacement binary, find a contemporary assembler that seems compatible, or simply preserve a ROM image forever and stop asking how it was made. Each option may be useful in an emergency. None is an adequate foundation for a machine whose behavior we want to understand and preserve.

Instead, the original assembler source was used to build a native host version, called `as9-host`. That choice did not make the work glamorous. It made it inspectable. The monitor could again be assembled locally from its own source, and the generated artifacts could be compared with the known baseline. A build was no longer a historical accident performed by a vanished operating system. It had become part of the present bench.

That is the first claim of this episode: when a build produces the bytes that a machine will execute from ROM, the build is hardware work. It belongs in the same chain of care as checking a clock, identifying a pin, or measuring a supply rail.

The point became especially clear in one small source change. An obsolete instruction had been removed during cleanup. The monitor still assembled. Its logic still appeared sound. But it was one byte shorter than before.

One byte is not an abstraction when a fixed ROM image is expected to occupy a fixed region of the address space. This monitor belongs at the top of a 16 kilobyte EPROM. The monitor proper is 2,048 bytes, and the full programmer image must reach the end of memory at hexadecimal `FFFF`. The reset vector must point to `F837`, where the processor should begin executing after reset.

The deleted byte therefore mattered. It shifted a layout that had been intended to remain exact. The repair was deliberately plain: retain the layout byte as a `NOP`, a no-operation instruction. The result restored the 2,048-byte monitor, the correctly sized programmer image, and the known reset vector.

This is a useful corrective to the habit of describing software as weightless. Source code can be improved, tidied, or modernized in ways that are harmless when a linker and loader will rearrange everything at run time. A ROM image has a geography. Addresses are part of its meaning. A programmer does not recognize an unintended gap in that geography. It will faithfully write a technically valid but misplaced sequence of bytes.

So the image was checked in several ways: by size, by mapped address range, by reset vector, and by checksum. None of these checks proves that the monitor will work. But together they rule out a class of mistakes before a chip is asked to carry them. They turn “the build completed” into a more useful statement: this is the image we believe it is, in the place where the processor will look for it.

The next problem was the serial interface. On this board, an MC6850-compatible ACIA—the asynchronous communications interface adapter—occupies two addresses. `BE00` is the control and status register. `BE01` is the transmit and receive data register. The distinction follows directly from the wiring: the CPU's address line A0 connects to the ACIA's register-select pin.

That description is compact, but it is a contract. At one address, a write configures the device and a read reports its condition. At the other, a write sends a byte and a read receives one. If source code reverses those roles, it is not merely using an unusual convention. It is addressing a different device from the one on the board.

The inherited monitor did not consistently honour this contract. Its receive routine tested the transmit-empty status bit. Its transmit routine tested the receive-full bit. Early initialization wrote its reset and configuration values to the data register instead of the control register. These were not one error repeated. They were separate assumptions that happened to occupy the same tiny piece of source.

The repair corrected each path and added an emulator regression test for the register offsets and status-bit behavior. The emulator is valuable here, not because it replaces the board, but because it gives the register contract a continuing test. It can tell us if a later edit once again writes control values to the data address or waits for the wrong condition.

Yet the emulator could not settle the whole question. A model can reproduce a mistaken premise perfectly when both the model and the source share it. The decisive evidence had to include the ACIA data sheet, the actual A0-to-register-select connection, and observations made on the physical board.

At first, the physical board offered the old and unhelpful symptom: silence. A terminal window remained blank after reset. This is the point at which a project can become a theatre of guesses. Perhaps the ROM is wrong. Perhaps the clock is absent. Perhaps reset never releases. Perhaps the serial cable is crossed. Perhaps the monitor is sending something the terminal cannot see.

The disciplined response is not to choose the most vivid theory. It is to reduce the number of theories that remain possible.

The power path from the FTDI serial adapter was corrected and measured at the board. Reset was examined and found to release slowly through its RC network, rather than exhibiting the apparent digital chatter suggested by an unsuitable short capture. The 6809's E clock measured about 1.843 megahertz, as expected from a 7.3728 megahertz oscillator divided by four. Activity appeared on the lower address bus after reset. The ACIA's receive and transmit clocks were present at their expected rate. The ROM layout and reset vector had already been checked independently.

None of these observations says, by itself, “the monitor is working.” Their force lies in combination. The board had power. The processor left reset. It was clocked. It was fetching instructions. The serial device had its clocks. A blank terminal was no longer a mystery spread across an entire machine. It had become a bounded question about a smaller part of the system.

The measurements also made a methodological point that is easy to learn and easy to forget. A scope trace is evidence only after the measurement arrangement has earned trust. A missing or mismatched probe ground can create a comparison that looks persuasive precisely because it has detail. Before drawing conclusions from a split capture of the ACIA register-select signal and its transmit-data output, channels were rechecked on the same pin with a shared ground. Only then was the comparison worth interpreting.

The next clue was CTS: clear to send. On the 6850, when CTS is high, the transmitter's empty condition is inhibited. That behavior matched the symptom with uncomfortable precision. The ACIA could be active, the processor could be running, and the monitor could still wait forever for permission to send its first character.

There were two mistakes to correct before that clue could become an explanation. First, the relevant pin had been misidentified. CTS is pin 24 on this device; pin 23 is DCD. The data sheet settled that quickly. Second, a low-resolution schematic view made CTS appear unconnected. A temporary jumper from CTS to ground was installed as a diagnostic experiment. Immediately, the system came alive: ASSIST09 appeared, the RAM smoke test loaded and ran, and the monitor returned to its prompt.

That was strong evidence, but it was not a prescription to leave a wire in place forever. A jumper that makes a symptom disappear may identify a cause without being the right repair.

The routed PCB view supplied the missing fact. CTS, at pin 24, was connected to RTS, the request-to-send output, at pin 5. This board used local hardware flow control. The ACIA was not waiting for an external modem or a dangling input. It was responding to its own output.

The remaining question was therefore in the control byte. The previous initialization value was `51` hexadecimal. It selected the desired divide-by-sixteen rate and 8N1 framing, but it set RTS high. Since RTS was looped back to CTS, the configuration disabled the very transmitter that the monitor later waited upon. The code was waiting correctly for a condition that its own initialization had made impossible.

The repaired control byte is `11` hexadecimal. It preserves the serial rate and framing, keeps RTS low, and leaves transmit interrupts disabled. With that change, the temporary CTS jumper could be removed. A new full 16-kilobyte EPROM image was programmed, read back, and tested. The monitor spoke without external help.

This is the second claim of the episode: a correct setting is not merely a setting that contains the expected baud rate. It is a statement about the whole electrical relationship that follows from every bit in a control register. A hexadecimal byte is convenient shorthand; it is not an explanation.

Now we can return to the EPROM programmer. The chip used here is a 27C128, and the programmer is a Batronix Barlino II 32P. The ordinary sequence remains the right one: preserve a read of any existing chip, select the exact device, blank-check a replacement, program the intended image, and verify it.

But there is an important refinement to the word “verify.” A successful dialog from the programmer is useful, but it is not the only record. The final chip was read back as a complete device image and compared byte for byte with the programmer image. The resulting SHA-256 checksum was `7e564502d120123d82dc5fc04b62f397e79c95b15ff34fe09c73e75ebbce85a0`.

That long string is not meant to be recited as a magical token. Its role is much more modest. It lets a later person ask whether the file read from this chip is exactly the file that was intended for it. The answer does not have to depend on the memory of the person who watched the progress bar.

There is also a practical philosophy in using a small development rotation of EPROMs. A chip is not a sacred artifact merely because it has been burned. If a program is being developed, two reusable devices encourage each burn to answer a named question: does this image boot; does this configuration transmit; does this revised monitor load the smoke test? The repository preserves the evidence and the reason for the change. The chips remain instruments rather than becoming an expanding box of unlabeled near-misses.

The monitor was now correct enough to reveal one final layer: the host terminal. It is natural to think of the terminal as a passive witness. It is not. It sets pace, sends line endings, decides how to respond to echo, accepts keyboard events, and shapes the serial traffic that reaches a small, polled machine.

The first problem concerned S-record uploads. The Tcl terminal sender used to wait for a carriage return after each line. ASSIST09's loader deliberately suppresses echo and carriage returns while it is loading. The sender would transmit the first record, then wait for a reply that the monitor was deliberately designed not to send. Both ends were behaving according to their own rule. Together, they had no protocol.

The revised terminal recognizes S-record files and transmits them as a character-paced continuous stream. It does not demand an echo that the loader has promised to withhold.

The second problem concerned ordinary typed commands. Typing directly into the scrollback window delivered GUI key events immediately, bypassing the configured inter-character delay. A fast modern host can send a short command more quickly than a polled ACIA routine can reliably consume it. The result was a strange human experience: a command seemed to work only on its second attempt.

The repair queues direct typing and paces it at five milliseconds per character. The separate command-entry field remains the preferred route for complete monitor commands. Again, the lesson is not that old serial systems are fragile curiosities. It is that timing, focus behavior, echoes, and line endings are part of the interface contract. A host tool deserves to be tested as carefully as a board trace when it is carrying the program that will run on the board.

At this point, we can read the modest smoke-test result with more precision. The message did not emerge from a single lucky boot. It stands at the end of a chain: original source rebuilt on a modern host; a fixed image with checked size, range, and reset vector; ACIA access corrected against the data sheet and wiring; power, reset, clock, buses, and serial clocks observed; local RTS-to-CTS flow control understood; an EPROM programmed and completely read back; and a terminal whose loader and typing behavior match the monitor it serves.

That chain is what turns ROM burning from a ritual into an engineering act.

It also changes what “reproducible” should mean. Reproducibility is not the claim that a source file exists somewhere. It is the ability to take a declared source and toolchain, produce an identified image, place it in an identified device, install it in an identified board, use stated serial conditions, and obtain a recorded behavior. It is a path from text to machine conduct that does not rely on a private trick.

There is a useful humility in this standard. The prompt does not establish that the 6809 system is general, autonomous, or profound. It establishes something narrower and more valuable: there is now a known recovery environment from which further claims can be tested. The board can load a RAM-resident experiment. It can run it. It can come back. That is a real beginning.

The next phase does not require another blind burn for every idea. RAM becomes the fast loop: assemble, send, test, inspect, revise. ROM holds the stable beginning that makes those experiments possible. The distinction matters. A durable monitor does not end experimentation. It lowers the cost of honest experimentation.

So the final image for this episode is not really the glowing window of a chip programmer, nor a heroic scope trace, nor even the label on an EPROM. It is the prompt after a small program has run and returned:

`ASSIST09 RAM SMOKE TEST PASSED`

`ASSIST09`

`>`

The machine is not claiming to have solved a great problem. It is ready to receive the next one.

Thank you for listening.

## Research spine

- M6x09-II-SBC ASSIST09 bring-up record: reproducible `as9-host` build, fixed monitor layout, ACIA repair, board measurements, RTS/CTS loopback diagnosis, EPROM readback, and terminal workflow.
- MC6850-compatible ACIA data sheet: register-select behavior, status flags, modem-control pins, and control-word semantics.
- ASSIST09 monitor source and emulator regression: serial register offsets and transmit/receive polling behavior.

## Drafting note (not spoken)

The checksum, addresses, control-byte interpretation, scope observations, terminal behavior, and physical pass condition in this draft are drawn from `episode-13-assist09-bring-up-reflection.md`. Before recording, retain the exact linked technical records and board identifiers with the episode materials so the spoken account remains traceable.
