# Episode 6: A Four-Bit Wonder

Welcome to Episode 6 of *The Last Cyberneticist*.

This episode is called *A Four-Bit Wonder*.

In the last episode I talked about the early AIBO ERS-111, behaviour diagrams, and the value of making a machine legible rather than just an impressive work of art or technological sophistication. I think one of the deepest virtues a machine can have is intelligibility. Not because that makes it less interesting, but because it gives us traceable behaviour: something we can catalogue and make answerable to the cognition we expect from things, and the expectations we place on objects. It gives us some chance of saying what the system is doing, why it changes state, and how it regains coherence after disturbance.

So this episode stays with the same concern, like all the episodes, but I want to take it somewhere else. We can look at a finished product and identify certain features of its behaviour. But in doing that, other than looking at the scripts themselves, we are obscuring how this actually happens.

As you may or may not know, computers talk in binary: zeroes and ones. It is in all the movies, and a lot of people say it, clearly, I hope. Higher computing languages - assembly, C, Forth, Java - are higher levels of abstraction from that. But at any point, the machines are running zeroes and ones, because you are dealing with silicon, transistors, and gates. We have to keep that in mind.

So we have this higher-level abstraction of behaviour, with all the things we like about it. How does it come down to zeroes and ones? Instead of trying to explain it, or trying to convince myself that I know what I am talking about by explaining it, I am going to discuss actual builds.

We are going to begin like this.

There is an interesting article - I would anticipate that people would find it interesting if they read it - in the August 1950 issue of *Astounding Science Fiction*. It is called "How to Build a Thinking Machine." It was written under the pseudonym J. J. Coupling, by the physicist John R. Pierce.

I only recently discovered that in the early 1950s, when artificial intelligence, robotics, and these kinds of things were discussed from a scientific perspective, a lot of authors put them in science-fiction magazines because that was where the readership was.

Pierce was not somebody at Saturday University. He was somebody doing real physics with machines at the time. There is a little context here: from Turing's work, through the impetus of cybernetics after the Second World War, you get this prehistory of machines and then the real history - which is what we are doing now. This article is right on the cusp of that.

What is interesting is not only the machine idea. It is a short article, with schematics, which always gives something a bit of credit. It is the skepticism the author has about it. Coupling, or Pierce, was already pushing back against inflated claims about thinking machines in August 1950.

He observed that the people actually building large electronic computers were pretty modest about the claims they wanted to make. The people who knew something were making interesting claims; people who knew nothing were making really bold claims. Maybe it was not called AGI at the time, but that particular behaviour has been going on the whole time in this field. We should not be surprised when we hear it now.

What is interesting about Coupling or Pierce is that the skepticism is not cynical. He starts to talk in terms of architectural discipline. The optimism and the vision of creating new things are not shot down, but language is not allowed to outrun buildability.

What can you actually make that proves that?

I think that is a really interesting mix. Instead of looking at some great machine - an AGI thingy, which we do not even know what that is - you bring it down to a much narrower and better question: what would count, even in rough form, as a machine that learns? What are the features that make that possible?

That question is still valid on this day, 27 August 2026. It never left the field. It is still here, running around.

So, looking at Coupling: he answers it in a very plain way. A machine should not be entirely predictable. It should contain some random elements. It should not learn from one lucky success and say, "Oh, that is great. I am going to stay there." It should be shaped by repeated successful passages - successful operations.

How does he quantify that? He talks about mazes.

His discussion of mazes, in terms of binary, is interesting. It is not just a puzzle. He talks about the probability of navigating a maze on the basis of the sequence, the bias, of the ones and zeroes as they come in: whether the thing goes from the left side to the right side. You can see that the probability of going one way is greater than the other just from how the numbers are set up.

It is an architecture-aware environment. That is all it is. In that environment, branching, choice, error, success, memory, and revised conduct are visible without too much confusion. The world is constrained enough that we can tell what the machine is doing and when one routine begins to dominate another.

That is how you start to understand what it is actually doing, versus what the noise is telling you that you think it may be doing. That is why Coupling, or Pierce, is important. The skepticism does not shut the conversation down; it leads to experimentation, controlled settings, machines that can try, fail, receive consequence, store biases, and gradually change behaviour over time. Again: in time, remember that.

Today we would recognise that as leading toward primitive machine-learning setups, but there is no fanfare and ceremony. It is sober and down to earth. That is what I admire about it. It does not wave its arms around and make crazy claims. It just describes a machine that adjusts.

That intellectual weight from Coupling leads into what David L. Heiserman was doing with Rodney and the other robots in the early 1980s. I cannot say there was direct influence. Heiserman was well read and worked around physics, and he might have known Coupling's work, but I am not saying that a direct influence has been found.

The maze could be a coincidence. But maybe it points to a thought process that we humans also find ourselves in. This is a subtle point: perhaps by looking for an architecture-based description, we discover that our own thought processes are architecturally based in time. The self-similarity of that, within ourselves and the machine we are creating, is comforting to me. I am not stepping outside myself too far; I am using my mind to construct another mind, if you will, or another object that operates in an environment.

I do not know that for sure. But it puts me in that direction and makes me want to keep working toward adaptation and the idea of the maze. It is not something I will probably work on directly, because I have a different set of motivations that I will get into in later episodes. But the constrained world of route choice, reinforcement, memory, and revision is an honest observation, and we have to get to that point.

If you want to come into this field, this is where you have to start. Coupling is the stripped-down version of the problem. Heiserman is a more developed behavioural form. There are a lot of interesting features to it, but it is still the same basic question.

I talked about Heiserman's codebase in the previous episode, and I will go into it again. To summarise: if the code we are working on is organised around state, route choice, consequence, retained history - remembering and forgetting - and altered future behaviour in a constrained environment, then these are all in the same line of thought.

So let me pivot to something we can do to start to test these ideas.

I put together a device. I guess I can call it that. It is a handmade board, a little test platform.

Let me start with some background. When you build a computer-like circuit, it has integrated circuits - ICs. I have one in front of me that I am looking at while I describe it: a chip, a piece of silicon in a plastic case, with what is called a dual inline package, a DIP, and pins down either side. The one I am looking at has 20 pins. Another one, an NMOS ROM, has 28 pins and is a bit wider.

You have these pins coming off the bottom and then you think: okay, what is next? When you look at a circuit board, you see a board and all the lines running inside it, connecting ICs and passive components. We will get into the details later, so do not worry about remembering that for now.

But the fundamental question you have to ask at this point is: how do I make a wiring pattern that does something?

When I started working on this back in the day, I tried making circuit boards. Copper-clad board, an ink pen to scribe the schematic and the copper runs, then an acid bath to remove the parts not covered by ink. It works, of course, but I did not like it. It was messy and ugly.

The other option is wire wrapping. Wire wrapping is actually very sexy. You take an IC and put it in a wire-wrap socket. These come in all the configurations that ICs can plug into. You put them on a piece of protoboard, basically a perforated board with holes at a spacing that matches the socket pitch. Then you use a special tool and a special kind of wire and literally wrap it around the posts. That creates all the wiring connections between the pins.

That is wire wrapping. I would recommend it. It is a very wholesome activity and you get to know the circuit you are building very well.

The four-bit wonder - there is a picture in the artwork, and I can put some more pictures on the Substack - has two parts.

At the top left is a timing-divider circuit. To bring Coupling's ideas into something we can actually test, I wanted to divide a frequency into what I call an octave-based spectrum. All those fancy words mean that each frequency is mathematically related to the other by a simple ratio: two, four, eight, like octaves on a piano. It is clean and obvious. These are low-frequency things, in the hertz range and low kilohertz.

The lower part is a small memory environment. The idea is a small machine where you can set patterns by hand, watch them appear in lights, read simple values, and check whether the memory is holding them. I set the switches, see the lamps light up, click, and see whether it has been saved and stored.

At the bottom left are the red lamps and six switches. That is the address. The blue lamps on the right show what is saved in memory - what is present in memory. At the top right are the control switches: chip select, which connects the chip to the bus; write or read; and the push button that lets you do that.

That gives me a chance to ask: what does memory look like? What does memory do? What does it mean for a machine to hold something?

We have state: the value at an address, and the data itself. Because it is only four bits, it has four lights. That is pretty straightforward and not too complicated. I can see switching, timing, read-back, and real signals on simple memory. The amount of time it took to build it, versus the time spent playing with it, means you get the sense of how it works really fast.

The memory is a 2114 static RAM: four-bit, one kilobyte, I believe. As long as power is applied, the values stay in it. You can prove that it is doing its job. We are not dealing with textbook abstractions; we are dealing with real things. This is computing. We are not at a whole computer yet, but we are doing the basics. We need timing because we will need to deal with a CPU. We need memory. We need a bus to carry values from the switches. The switches have a voltage on them, and the bus is the channel that brings those values into the static RAM.

Briefly, on power: I have some photos of this and maybe I will put them on the Substack too. I am always trying to make things as uncomplicated as possible. What I want to achieve may be complicated enough already; I do not want to bias it with tendencies that make me think about it in a certain way. I want to remove the possibilities of weirdness.

So I use a little phone battery - I think it is supposed to be wireless-powered - with USB, and the positive lines come out to two clip leads. The clip leads are from an old HP signature analyser. They are quite handy when repurposed. The voltage comes in there, and I have a mobile-phone battery and a couple of clip leads powering the board. I can be confident that nothing else is coming in from the side and affecting the state, or becoming some other external variable.

I am isolating the system, making sure it has everything it needs, so that I can start to think about the variability I observe and the novelties I might discover.

With the four-bit wonder, the power-on state is interesting because it leads back to Coupling and this necessity of randomness. But it is important to be precise: after power is removed, a static RAM has no defined contents. The LEDs can show a different four-bit value at a selected address on different power-ups. That is an observable start-up condition of a volatile memory system, not reliable information preserved while the power was off.

I have not done a full experiment on it. I have observed that, across repeated power cycles, it does not present the same value every time. I would say maybe two in ten, one in five. That is not a conclusion; it is an observation. Still, it is something you do not have to program in as the engineer. It comes from the physical system.

That is the part worth paying attention to. You can look at the physics: silicon dioxide, copper, maybe aluminium; metals, semiconductors, conductors; different properties, different manufacturing conditions. You do not have to control everything. You can observe a natural system.

That is what I think the four-bit wonder is really about. It is a disciplinary device. The argument does not outrun the mechanism. The memory is physical, the control is visible, and it helps you understand what comes later. You can trust what you are looking at because you are not waving your arms around and making crazy claims. You are looking at how it actually exists.

That is the great takeaway of the process. It becomes serious: a place to preserve, check, and reintroduce things on purpose.

Thank you for listening.
