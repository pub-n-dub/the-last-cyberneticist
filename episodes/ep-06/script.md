# Episode 6 Script

## Title

`A Four-Bit Wonder`

## Script

Welcome to Episode 6 of `The Last Cyberneticist`.

This episode is called `A Four-Bit Wonder`.

In the last episode, I talked about the early `AIBO ERS-111`, behavior diagrams, and the value of making a machine legible rather than merely impressive. One of the deepest virtues a machine can have is intelligibility. Not because intelligibility makes the machine less interesting, but because it makes the behavior traceable and answerable. It gives us some chance of saying what the system is doing, why it changes state, and how it regains coherence after disturbance.

This episode stays with that same concern, but I want to take it to a different place.

When we look at something like `AIBO`, we are looking at a finished object. We can identify features in the behavior and we can describe what seems to be happening. But unless we go back beneath the finished surface, we are still obscuring how any of that actually happens.

So this episode comes down to something more basic.

As you may or may not know, computers speak in binary. Zeroes and ones. That shows up in films and popular culture so often that it can become a cliche, but the underlying point is still true. Higher-level languages, whether assembly, `C`, `Forth`, `Java`, or anything else, are abstractions built upward from that. At every point, the machine itself is still dealing with transistors, gates, and binary state.

We have to keep that in mind.

Because once we start talking about behavior at a high level, the natural question becomes: how does any of that come back down into zeroes and ones?

And rather than trying to answer that only through explanation, I want to answer it through actual builds.

So let us begin there.

There is an interesting article from August 1950 in `Astounding Science Fiction` called `How to Build a Thinking Machine`. It was written under the pseudonym `J. J. Coupling`, but the author was `John R. Pierce`, a physicist who was well placed in the technical world of his time.

I only recently discovered that in the early 1950s, when people were talking seriously about machine intelligence, robotics, and related scientific questions, some of that work appeared in science-fiction magazines because that was where the readership already existed.

That matters a little historically, but what interests me more is the article itself.

It is a short piece, and it includes schematics, which already gives it a certain kind of seriousness.

But what struck me most was not only the machine idea.

It was the skepticism.

Pierce was already pushing back against inflated claims about thinking machines in August of 1950. He observed that the people actually building large electronic computers tended to be more modest in their claims, while the people furthest from functioning machinery were often the boldest in what they were willing to promise.

That pattern should sound familiar.

It has been present in this field for a very long time.

So we should not be surprised when we hear it now.

What is interesting is that Pierce's skepticism is not cynical. It does not shut down the discussion. It becomes a kind of architectural discipline. The optimism is still there. The possibility of building new things is still there. But it is governed by a refusal to let language outrun buildability.

In other words:

what can you actually make that proves the point?

That is a very good question.

And it leads Pierce toward a much narrower and better one:

what would count, even in rough form, as a machine that learns?

That question is still with us on Thursday, August 27, 2026.

It never really left the field.

Pierce answers it in a very plain way.

A machine should not be entirely predictable.

It should contain some random element.

It should not learn from one lucky success and then freeze there forever.

It should be shaped by repeated successful passages.

And then he places the whole problem inside a maze.

That move is more important than it may first appear.

His discussion of the maze is not just puzzle talk. It is a way of setting up a constrained world in which the probabilities of route choice can be made visible through binary sequences and repeated passage. One route begins to dominate another because the conditions are bounded tightly enough that the machine's behavior can be observed rather than merely imagined.

That is why I have called it, perhaps a little awkwardly, an architecture-aware environment.

What I mean is simple enough.

In the maze, branching, choice, error, success, memory, and revised conduct can all be made visible without too much confusion. The world is constrained enough that we can tell what the machine is doing, and when one routine begins to dominate another.

That gives us a very useful starting point.

It lets us understand what the machine is actually doing rather than what noise, rhetoric, or wishful interpretation might tell us it is doing.

That is why Coupling, or Pierce, matters here.

The skepticism does not shut the conversation down.

It leads toward experiment.

Toward controlled settings.

Toward machines that can try, fail, receive consequence, store bias, and gradually change their behavior over time.

And yes, from our present vantage, that begins to look a lot like a primitive machine-learning setup, but without fanfare and without ceremony.

It is just sober and down to earth.

That is what I admire about it.

It does not wave its arms around.

It simply describes a machine that adjusts.

And that intellectual weight leads very naturally into what `David L. Heiserman` was doing later with `Rodney` and with robots in mazes.

I cannot state that there is direct influence there.

I do not know that.

Heiserman was well read and moved in adjacent technical territory, so it is possible he knew Coupling's work, but I am not claiming that as a proven line.

Even if the recurrence is coincidental, it still matters.

The return of the maze across time suggests a logical progression in how people think about machine adaptation. If you want to study route choice, reinforcement, memory, and revision inside a constrained environment, the maze keeps returning because it is such an honest way to stage the problem.

There is also a subtler point that interests me.

By looking for architectural descriptions in the machine, we may be discovering that our own thought processes also seek architectural form through time. I find that strangely comforting. It means I am not stepping entirely outside myself. I am using one mind to construct another object that has to operate in an environment.

That does not prove anything mystical.

But it does suggest that the progression from Coupling to Heiserman is not arbitrary.

It follows a recognizable line of thought.

And that line also gives firmer footing to the codebase we have already discussed. If the code is organized around state, route choice, consequence, retained history, remembering, forgetting, and altered future behavior inside a constrained environment, then it belongs to this same line of thought.

So let me now pivot to something we can actually build in order to test these ideas.

I put together a device, I suppose I can call it that. A handmade board. A small test platform.

What does it do?

In plain terms, it lets me set patterns by hand, watch them appear in lights, write and read simple values, and check whether memory is really holding what I think it is holding.

Why build something like that?

Because before you trust a larger machine, it helps to have a simple one where state, change, timing, and retention are visible directly.

That is the `four-bit wonder`.

To explain why I built it, I need to step back for a moment.

When you want to build a computer-like circuit, you begin with integrated circuits. These are little chips in plastic packages with metal pins on either side. One of the chips in front of me as I think about this has twenty pins. Another, an `NMOS ROM`, has twenty-eight pins and is a bit wider.

So then the immediate question becomes:

how do you make a wiring pattern out of these things so that the result actually does something?

When I first started working on circuits years ago, I tried making etched circuit boards directly. Copper-clad board, ink pen, acid bath, all of that. It works, but I did not like it very much. It was messy and ugly.

The other option is wire wrapping.

And I have to say, wire wrapping is actually rather lovely.

You take an integrated circuit and place it in a wire-wrap socket. You mount those sockets in a perforated protoboard. Then, using a special tool and a special kind of wire, you wrap the wire around the posts to create the wiring pattern between the pins.

That is all it is.

And I would recommend it, because it is a very wholesome activity and you get to know the circuit you are building intimately.

In the `four-bit wonder`, there are really two parts.

On the upper left is a timing-divider circuit.

On the lower portion is a small memory environment.

The timing side was there because I wanted a frequency structure that could be divided into a simple octave-based spectrum. That sounds more elaborate than it is. All it really means is that each frequency is mathematically related to the next by a clean ratio such as two, four, eight, the same sort of clarity you get with octaves in music. That gives low-frequency signals that are obvious and easy to reason about.

The lower portion is where the memory work happens.

There, the idea is to have a very small machine where I can set patterns by hand, watch the lamps respond, write values into memory, and then verify that those values have actually been retained.

On the lower left are the red lamps with their switches.

Those correspond to the address.

On the right are the blue lamps, which show what is actually present in memory.

On the upper right are the control switches: chip select, read and write, and a push button that lets the action occur.

So immediately we get a much clearer sense of what memory means in practice.

What does memory look like?

What does it mean for something to be held?

What does it mean for state to be visible?

Because it is only four bits wide, it stays legible. Four lights. Four bits. Not too much to keep in your head at once.

That makes it a very good place to start.

I can see switching.

I can see retention.

I can see timing.

I can see readback.

I can see real signals moving through simple memory.

And because the device is so modest, you get the sense of how it works very quickly.

The memory device itself is a `2114` static RAM.

With something like that, you can begin asking very concrete questions.

What happens on power-up?

What state is retained in the silicon?

Does a charge remain?

Does the memory come up in the same condition every time?

Or does it not?

That is interesting, because it pulls us back toward Coupling.

He says a learning machine should have some random element.

And here, in a very small and material way, the `four-bit wonder` exhibits something like that at power-on. Depending on how long the system has been off, depending on what has dissipated and what has not, the board does not always present exactly the same values every time it starts.

I have not done a full formal experiment on that yet, so I do not want to overclaim it.

But from what I have observed, the power-on state does show some variability. Roughly speaking, perhaps two times in ten you will see something different enough to notice. That is not a polished conclusion. It is an observation. But it is a useful one.

Because it means there are features in the system that I am not explicitly scripting as the engineer.

Something is entering from the physical reality of the components themselves.

That is worth paying attention to.

It makes the setup feel a little more natural, not in a mystical sense, but in the sense that the materials themselves are participating. Silicon, copper, capacitors, conductors, semiconductors, fabrication differences, residual charge, timing of dissipation. All of that becomes part of what can be observed.

And that, to me, is one of the reasons to build something like this.

We are not dealing only with textbook abstractions.

We are dealing with real things.

We are saying: this is computing.

We are not at a complete computer yet, of course, but we are working through the basics honestly. Timing matters. Memory matters. Buses matter. Voltage on switches matters. The values have to move through real channels into real memory.

That is already enough to learn a great deal.

There is another reason I wanted the power arrangement to stay simple.

Whenever I am working on something like this, I want to reduce unnecessary complication as much as possible. The questions I care about are already difficult enough. I do not want to load the setup with extra variables if I can avoid it.

So I powered the board very simply, using a small phone-style battery supply and clip leads. The clip leads themselves came from an old `HP` signature analyzer, and they are still quite useful when repurposed.

That gives me confidence that I am looking at the system itself rather than some surrounding confusion.

I want to isolate the setup well enough that I can begin to notice real variability and real novelty when they appear.

And that leads back, once again, to the central point.

The `four-bit wonder` is a disciplinary device.

It keeps the argument from outrunning the mechanism.

Memory becomes physical.

Control becomes visible.

And the things that will matter later can be studied in a setting small enough to inspect directly.

That is why I think it matters.

It is not because it is powerful.

It is because it is honest.

It is also, importantly, makeable.

Not easy in every respect.

Not costless.

Not guaranteed.

But makeable.

And that matters because it reminds us that computing does not have to remain the property of giant institutions and sealed products. A person with simple tools, modest parts, patience, and care can still build meaningful fragments of a machine and learn from them directly.

That may sound like a small point, but I do not think it is small at all.

If we want serious experimentation without too much bias built in, we need places to begin that are simple enough to understand and concrete enough to test.

That is what the `four-bit wonder` gives me.

Now, this also reveals a limit.

Static RAM is excellent for exploration because it lets us set, change, and inspect values directly. But if we are moving toward more durable behavior in a machine, then sooner or later we need more than exploratory state. We need program placement that can be written deliberately, verified, removed, stored, reinserted, and expected to return the same way later.

That is where ROM enters the picture.

And that is the next threshold.

The next step is not only to store a bit.

It is to turn software into a memory device that the machine can actually carry.

That means programming chips.

It means verification.

It means handling, compatibility, and retention.

It means recovering a more material loop in which software is not merely written, but physically placed.

That is where this line of work goes next.

Because the process becomes serious when behavior can be placed, preserved, checked, and reintroduced on purpose.

Thank you for listening.
