# Episode 7: The Benefits of Remembering

_Generated from a local Whisper transcription of the published recording, then lightly cleaned for obvious recognition errors, proper nouns, and broken phrasing._

Welcome to Episode 7 of *The Last Cyberneticist*.

This episode is called *The Benefits of Remembering*.

I want to begin slightly differently than I have in prior episodes.

In a piece called *Recollection*, Alan Watts treats remembering as recognition rather than acquisition: noticing what has been overlooked beneath the social role, the persona, that we mistake for a complete self. In a related thought, if experience left no trace beyond an instant, there would be no way to know it had happened to you. There would be no continuity from which a life, a self, or a sequence of actions could be recognised.

What I just read is not a technical definition of computer memory. However, to remember is to allow a persistent state to stand in relation to what came before it. I am saying this in a particular context.

A machine does this in a tiny, very literal way. It holds a chosen physical condition long enough for another operation to find it again. With not too much stretch of the imagination, you can see a correlation between biological remembering and machine remembering. But do not take it too far just yet.

In the last episode I introduced a little board. It is called the four-bit wonder. It is a very small, very plain machine for making state visible. There is no way to obfuscate or propagandise any output or solution. It is there to show exactly what is visible: state visibility.

I have talked about the board as a disciplinary device, which I think is the right description. In later episodes I will go into exactly what that means. For now, it keeps descriptive language from outrunning the mechanism itself. It keeps us from letting our imaginations take flight. It makes memory physical, makes control visible, and gives us a place where timing, switching, read-back, and retention can be inspected directly instead of assumed.

Because remembering is important, I want to go through more of the board's general-purpose characteristics: the parts we should focus on for this task and for what is coming up. The central part is the 2114 static RAM, or SRAM. There are the lamps and the switches. I hinted at startup variation and the value of a simple power arrangement last time. That was a first pass.

It is not enough as we start moving into artificial intelligence, machine intelligence. We need to drive home this particular understanding. It is not enough to say, "Oh, it is remembering. Oh, it is learning from that memory system over there." They pay, what, fifty thousand a year for people who can write self-improving programs - self-programming, in the old books. They told us we were not supposed to do that back in the day, but they are paying lots of money for it now.

We need to understand what remembering actually means in a machine.

How does it do that? How does a remembered state become a physical event? How do those little integrated circuits - the little black rectangles with metal pins sticking out of the side - become an addressable system? How do switches become numbers, numbers become locations, and a selected location yield a visible result?

Why bother doing this by hand, spending all that time, when the modern machine already does it all for us? It has been doing it for a very long time.

That is the real question for this episode.

I think it is wise to stay with the four-bit wonder a bit longer. Let us linger here and look at the details and where they can take us. Not because it is a great or powerful machine, but because it is real and small. It does not allow us to be subjected, either by choice or design, to smoke and mirrors.

That has been the argument of this podcast for a long time: we have been subjected to an illusion and placed on a wheel that we cannot escape. There is only one way to escape, and that is through this rare and valuable combination.

So let us start here.

When people say computers are made of chips, the phrase is so common that it almost ceases to mean anything. A chip sounds like a tiny magical object, a sealed unit of intelligence. But an integrated circuit is better understood as a dense arrangement of ordinary electrical functions brought together inside one package. It integrates components and connections into something small enough, cheap enough, and reliable enough to become useful.

Historically, people were wiring huge numbers of separate transistors, vacuum tubes, resistive structures, and other elements in open spaces. Those spaces were large. With integrated circuits, the transistors, resistive structures, capacitive elements, and silicon are manufactured together in a substrate.

The package is not intelligence. It is the container that lets a designed electrical organisation meet the outside world through pins.

It does a lot of hard, time-consuming work and gives it to you in a neat little place, at a neat voltage. You do not have to focus on every physical aspect of making the system work. You can look at a book, decide which chips you need, and start wiring them together because you know the pinouts and the outputs.

That pin arrangement is the part that really matters. A chip becomes part of a system when its pins are given a role: power, ground, address lines, data lines, control lines, clocks in some designs, enable signals, read, and write. Those words describe the relationship between the chip's internal organisation and the external wiring pattern. They give you the ingredients for a larger machine.

That is why I like wire wrapping so much, as opposed to making an etched circuit board.

When I started, I built circuit boards. With etched boards, a lot of the logic disappears into the traces. You draw the circuit diagram: this goes here, this goes here. But you do not really get the sense of it. There is something about the physical act: something in your mind, something with your hands, and seeing the result play out in front of you.

You have to lay the chip in next to the parts it should connect to. You do not want very long wires. There has to be thought about how the pieces are placed next to each other, so the lines are short and you do not consume all your stock of wire-wrap wire.

Over time, you get a feeling for the curvature of the wires. You cut the wire, strip the insulation to the right length for the tool, set it up, wrap one side, then the other. By repeated wire wrapping, a nice curvature starts to come out. Then you start to think about colours: red for voltage, black for ground, yellow, green, red, and blue for different functions - control, bus, addressing.

That creates a whole set of connections that you commit deliberately in your mind. It is a skill that improves like riding a bike. The more you do it, the more fun and personally satisfying it becomes to see things work.

I get my schematics, look at my data sheets, look at the pinouts, and start to architect the wires. But it is not something you only think about. You just do it. You wrap it, and you see, "Oh, this should go like this, like that." It comes out as part of a creative process.

People will criticise you for saying, "Oh, you are such a technical person. It is so technical." At this point it is artistic, because it is an expression. Everybody will do it differently.

That does not make wire wrapping superior. It is verbose. But for learning, and for getting the sense of what you want to achieve, it is absolutely right for that. The four-bit wonder is not just a memory board. It teaches by exposing relationships.

Let us look at the 2114 static RAM. It is toward the middle of the board, aligned vertically. It is RAM: random-access memory. It holds a state, a number, and its contents can be changed during operation.

Static RAM is neat because it does not require the refresh cycles associated with dynamic RAM. With static RAM, as long as the device is powered and the signals meet the timing and control expectations of the chip, the stored state remains available.

I chose it because it is small enough and basic enough that everything feels manageable. It is 1024 by four: four bits wide. Hence, four-bit wonder. It is the simplest expression you can come up with that can still make meaningful things.

When memory is discussed at a high level, people imagine an abstract expanse. A machine has memory. A program uses memory. Data sits in memory. But we have to get to the idea of selection. Memory only becomes useful when a specific place can be chosen. That is what an address is.

An address is not an ethereal coordinate. It is a pattern presented to a set of lines so that one location is distinct from another. On the left side of the board you see the resistor bank and the two ICs above it. Addressing requires two separate ICs, the bus itself, and an inverter. Signals are pulled high and low, and their inversion gives the stability needed for the switches and LEDs to show their inputs and outputs.

The red LEDs at the bottom left, with the switches, are the visible statement of the address bus. From right to left you get ones, tens, hundreds, thousands, ten-thousands, and hundred-thousands: a six-bit address.

That is the epistemology of it. The address selects the place where I want to put a value. When I set address one, I can put data there, and it stays at address one.

It is a tiny form of dialogue. I assert a piece of data that I select, and it is placed inside the address. That assertion is a feedback structure. That is the subtlety that connects this board to the philosophy of the whole project.

When we later talk about programs, experiments, behaviour loops, and learning, we are still talking about systems where a state is established, a consequence follows, and the result is checked against what was expected. It is the relation between command, state, verification, and the humble importance of buses.

The word "bus" can sound grand, but it is simple: a shared group of lines used together for a role, such as addressing or data transfer. The address bus specifies location. On the right, the data bus carries the value. There is another resistor bank for pull-ups and current limiting for the LEDs - you do not just plug an LED into a power source.

There is also an Intel 8226, a very old and hard-to-find but reliable bus device. It allows a value to be carried one way when it is written and the other way when it is read.

Thinking in buses helps with larger concepts because it stops us staring at wires as only wires. A single wire carries a bit. A bus carries a number, or at least part of one. Once the board is understood this way, it starts to simplify. It is not a jungle of connections. It is a small set of organised paths with distinct jobs.

That is the simplification we need before we scale into larger memory, ROM, control, and placement. If I, or anyone, cannot mentally manage an address bus and a data bus, then we cannot begin a discussion of more elaborate systems.

Artificial intelligence is a complete bloody illusion. But rather than merely saying that, we can build systems that demonstrate what an intelligent machine might actually be away from that illusion.

Manual programming by switches is an extremely valuable exercise, not only for your mind but for communicating the proof we are looking at. It could be a kind of moral education, perhaps. I am not going to pontificate. I am not a holy man. They can call me a scientist; they can call me a lot of things.

I try to keep myself free from bias because I am looking for the truth. I want to understand what something is really about. University helped a great deal in formulating questions. You can start to disentangle yourself from what you were told or taught and ask what to investigate, and how.

When you are younger, that can give you motivation and impetus. Later, you can say, "Artificial intelligence is complete crap." Okay. But how does that actually help anything? Let us stay with wonder instead. The lower world becomes impossible to ignore because you are building from first principles and creating logical arguments in terms of topology. That is incredibly satisfying.

One of the most important things I glossed over last time was the power system.

We have discussed the address. Forget the top left for now; I am going to phase that out because it is a distraction at this point. At the lower left is the address. In the centre, vertically, is the static RAM. On the lower right is the data bus with its four blue LEDs. Directly above that, the four switches select the value that you want to place on the data bus. It is the same logic as the address: ones at the right, then tens, hundreds, and thousands. You can create 1011, the highest value you can place in an address. Then there is chip select, read/write, and the pushbutton, which gives you a nice, deliberate action: I am going to set that up and put that in there.

One interesting thing I picked up from another professional was using passive components - resistors - inside wire-wrap sockets. You can include the things you need without interrupting the creative process of putting the machine together. It is still like another IC construct.

If you take a socket made for wire wrapping, you will see that the posts are square, not round. When you wrap wire around the square post, the sharp edges create what is basically a cold weld. The connection does not come free unless you unwrap it with the same tool. My tool has one side for wrapping; you unscrew it, flip it, and it has the unwrapping side.

The contact is so strong that wire wrapping was used in aircraft. Think about the vibration up there. With the four-bit wonder and projects like it, you are building something to last. I am not creating something just for now and for fun, then forgetting about it. I can dedicate myself to it creatively because if I set it aside for one, two, or five years, I can come back and it will still work.

The final thing I want to talk about is the power system. The first instinct is to grab a five-volt supply. Fine, but I have to plug it in somewhere. Depending on where I am, this has 230, this has 115, that has 100, that has 220. There are variations depending on the place. You also have to carry something rather heavy, with transformers in it.

So I took a mobile-phone battery - a power bank. I touched on it last time, but the satisfaction of using a stable power supply has its own trigger: safety. If something is not wired correctly, nothing will smoke. It has its own safety margin.

On my Substack I have a little sequential diagram of going from USB-A to these Hewlett-Packard Signature Analyzer clips. It is a safe, small arrangement. It lets you put these things together safely, and it is reusable.

When you put those concerns in the background, you can look at the machine: observing, loading, revising, testing, repeated experimental loops. This convenience strips away what you have to worry about and focuses on the grammar we are creating.

What is that grammar? Address, data, control, selection, read-back, retention, and verification.

That is extremely healthy. It gets us back to how I began this episode with Alan Watts. Recollection - remembering something - is an act of existence. In his reflections on death, he provides the counterweight. When Watts says memory makes intelligence possible, but unbroken accumulation leaves no room for renewal, the value of remembering requires forgetting.

The four-bit wonder gives that idea a technical form. We have a known clear state. If we write to the same address, we intentionally overwrite. A reset is not memory's enemy. It creates a meaningful next pattern.

At startup, after power has been removed and brought back, SRAM has no defined contents. That initial state can appear random, but it is not retained information. It is an undefined volatile startup state. It is still important to bring that into the discussion and think about it.

We are trying not to hide things under layers of convenience. We want clear workflows where state and behaviour can be loaded, tested, revised, and repeated. We can test in different contexts, get to our philosophical context, and check: is it like that? We can eliminate the other things and say, okay, this is what we have. You are not being deceived because there are no other layers. It is binary numbers going into these places.

It is a serious attention to durable program placement, host-assisted interaction, and the beginning of a true experimental loop.

That is where we are going next.

Thank you for listening.
