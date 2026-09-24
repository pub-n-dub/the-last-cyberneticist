# Episode 10: Multenions: A Structured Algebra

## Script

Welcome to Episode 10 of *The Last Cyberneticist*.

This episode is called *Multenions: A Structured Algebra*.

Last time, we stayed with the Four-Bit Wonder long enough to make a simple claim. A light at the edge of a circuit is not automatically a fact. Before it can count as evidence, we have to know which word was present, which memory location was selected, which control state the machine occupied, which path carried the signal, and what operation was actually permitted.

That discipline gave us a finite physical arrangement whose configurations can be treated as a state system. The board has a bounded repertoire of conditions. A word can be present or absent on a path. A memory location can be selected. A read can be valid. A write can be valid. A comparator can report lower, equal, or higher. The possible situations are not infinite, and neither are the transitions between them. They can be traced.

Today I want to pursue a more ambitious question. What if we did not treat that trace merely as a description we draw after a machine has been built? What if states, relations, transformations, and their permitted compositions were themselves the material of a program?

That is the direction I want to introduce through Multenions: a structured algebra.

Multenions is not a new name invented for this series. It comes from Alexander McAulay, whose 1908 paper was called *Algebra after Hamilton, or Multenions*. McAulay worked in the long aftermath of Hamilton’s quaternions. He also published *Octonions: a Development of Clifford’s Bi-quaternions* in 1898, and returned to multenions in a sequence of papers on differential invariants in the 1920s.

The historical line needs care. It is tempting to say quaternions, then octonions, then multenions, as though each word named one simple ladder of ever-larger numbers. It does not. McAulay’s “octonions” were his name for a development of Clifford’s biquaternions; they are not the algebra now usually called the octonions. Multenions was his later attempt to systematize an algebraic method after Hamilton. In the record available to this project, McAulay appears to be its only sustained exponent. That is a research finding to be checked, not a claim that one name settles a theory.

This episode also does not claim that every finite-state controller is already McAulay’s calculus. It begins a more modest task: to see whether the insistence on named kinds of object, lawful operations, and explicit composition can be brought into contact with programs and machines we can inspect. The exact historical and formal correspondence has to be earned in the work that follows.

The word algebra can make a listener expect a blackboard full of symbols. Sometimes it deserves that expectation. But the first useful sense of algebra is much plainer. An algebra tells us what kinds of things we are dealing with, what can be done to them, and what follows when those operations are combined. It does not merely name objects. It makes their relations and transformations answerable to rules.

For this series, that matters because a finite-state program should be more than a list of instructions hidden in a processor. It can be pursued as an exercise in explicit algebraic objects. A state is an object. A permitted transformation is an object. A relation between states is an object. A composition is an object. A condition that blocks or allows a transition is an object. A trace of what happened is an object of inquiry as well.

This is not a claim that every flowchart is already an algebra, or that attaching mathematical language to a program makes it profound. It is a demand for enough structure that we can say what the program is made of, what it may do next, and why a particular result followed.

That demand is becoming more important because we now live among systems that produce striking results without always making their route to those results easy to recover. Much of contemporary AI is built from linear algebra and trained through gradient-based optimization. Large collections of examples become parameters. Those parameters are adjusted until a system becomes better at a specified task. The resulting system may classify, generate, predict, or control in ways that are genuinely useful.

None of that is being dismissed here. A gradient-trained system can be powerful precisely because it finds regularities that no person has written down one rule at a time. It can use a scale of examples and a density of calculation that a small explicit program cannot match.

But power and legibility are different virtues.

From the outside, a large trained system can sometimes feel like a search through a vast territory of possible answers. It is not literally a travelling-salesman calculation, and it should not be described as one. The resemblance is experiential: a procedure moves through an enormous space according to a rule of improvement, and eventually it arrives at a result that may work without offering a compact account of why this particular internal route was the one taken. At its most superficial, the relation to data can resemble trainspotting: immense collections of particulars are gathered, matched, and made statistically useful. What is difficult is not that the system has no structure. It has a great deal of structure. The difficulty is that much of the operative structure is distributed across learned parameters rather than presented as a small public vocabulary of objects and operations.

The contrast I want to make is therefore not intelligence against stupidity, or new technology against old technology. It is between two different ways of pursuing a machine. One way asks whether a system can find a useful answer from examples. The other asks whether the terms of its conduct can be made explicit enough to construct, inspect, change, and prove in public.

Multenions belongs to the second pursuit.

Calling Multenions a structured algebra means that its intended structure is not an afterthought. The elements are not merely numbers placed in a container and sent through a calculation. They stand in specified relations. The transformations are not merely whatever instructions happen to be convenient. They are part of what the system is. And composition is not merely putting one operation after another. It is where the system declares how one lawful change may become the condition for the next.

The important word is structured. Structure is what prevents a collection of marks from becoming an invitation to say anything we like. In a circuit, it is the distinction between an address line and a data line, between a selected memory chip and a deselected one, between a read condition and a write condition. In an algebraic program, it is the distinction between the kinds of object and the operations that may join them.

We can begin before any demanding notation appears. Imagine a small controller for a door. It has four named states: closed, opening, open, and closing. It receives a few named events: a request to enter, a fully-open sensor, a fully-closed sensor, and an obstruction signal. The controller has a few named transformations. A request applied to closed begins opening. A fully-open sensor applied to opening produces open. A timeout applied to open begins closing. An obstruction applied to closing returns the system to opening.

That is already a finite-state program. Its value is not that it is complex. Its value is that its possible conduct can be laid out without pretending the door has a hidden personality. We can ask whether the obstruction transition is present. We can ask whether a closed door can become open without passing through opening. We can ask whether there is a state in which no event is handled. We can test a trace: closed, request, opening, fully open, open, timeout, closing, obstruction, opening.

Now make the demand stronger. Do not leave those names as labels in a diagram. Treat state, event, transformation, and composition as explicit objects in the program’s account of itself. A transition is not merely a sentence in a manual. It is an entity that can be inspected for its source, its condition, its destination, and its consequence. A composition is not merely an accident of control flow. It is a declared way in which one transformation becomes available after another.

This is the kind of exercise Episode 10 is concerned with. The pursuit of finite-state programs becomes a pursuit of explicit algebraic objects.

There is a useful difference between an object and a value here. The number four is a value. But “the four that names this memory address,” “the four that is the current candidate,” and “the four that is the target” are not interchangeable objects, even when they share the same binary representation. Their roles determine what operations are appropriate. We learned that at the bench when the same four wires could be harmless data in one condition and a misleading apparent result in another.

An explicit algebraic program must preserve that distinction. It should not collapse every meaningful difference into an anonymous number, a bare memory location, or a line of code whose role has to be remembered privately by its author. It should make room to ask: what is this object; where did it come from; which relation does it stand in; what can act upon it; and what has to be true before that action is valid?

That does not mean every program has to carry a long philosophical explanation of itself. It means that the structure needed to understand its conduct is not treated as disposable commentary. It belongs to the construction. A good label can help. A type can help. A table can help. A physical separation of paths can help. But none is enough by itself. The question is whether the program’s stated objects and operations genuinely constrain one another.

Return to the door controller. A simple list of commands might say: if the obstruction sensor is active, command the motor to open. That can work. Yet several questions remain hidden. Is the door currently closing? Does the obstruction matter while it is already open? Does the command cancel a pending close, or merely add another instruction to the queue? What happens if the fully-open sensor never arrives? These are not edge cases added after the real program. They are part of the program’s possible conduct.

The structured approach brings those questions forward. It asks whether obstruction is an event valid in every state or only in certain states. It asks whether opening is a state, an operation, or both at different levels of description. It asks whether a timeout composes with an obstruction, and in what order. It asks what trace proves that the controller returned to a safe state. The result may still be implemented with ordinary electronics or ordinary code. What changes is the discipline by which its behavior is specified and checked.

This is why the contrast with opaque systems should not be heard as an argument against calculation. Explicit structures calculate too. They can be large, fast, and demanding. The difference is that their decisive transformations are intended to remain presentable as operations on named kinds of object. A listener, a builder, or a later repairer can follow a transition without having to reconstruct an entire history of training data and parameter adjustment.

There will always be tradeoffs. An explicit finite-state structure can become unwieldy when the world it describes has too many relevant conditions. A learned system may handle variation that a hand-specified controller cannot anticipate. But a learned system may also conceal a distinction that safety, maintenance, or accountability requires us to keep visible. The right question is not which method wins everywhere. It is where explicit structure is the condition of trust.

The phrase “exercise” matters. It does not mean the program is a toy. It means we learn the structure by performing it. We identify an object. We state an operation. We ask what composition is allowed. We test a consequence. We find an exception. We revise the account. A finite-state program becomes less like a spell that a computer happens to obey and more like a worked proof of possible conduct.

The Four-Bit Wonder remains useful here because it keeps this discussion honest. Its manual comparison does not yet supply a controller. It does not hold a target independently, decide a next action, revise a candidate, or verify a completed cycle. But it exposes several objects we would need: a remembered word, a target word, a relation between them, a valid read condition, a valid write condition, and a visible trace.

Suppose we wanted to make one small addition in thought, without claiming that the original board has already been changed. A controller could inspect the comparator. If the remembered word were lower than the target, it could transform the candidate upward by one. If it were higher, it could transform the candidate downward by one. If it were equal, it could stop. The states of that imagined controller might be capture target, read candidate, compare, step upward, step downward, write candidate, verify, and halt.

The point is not the particular arithmetic. The point is that each item can be named and distinguished. The target is not the candidate. A comparison is not a decision. A decision is not a write. A write is not a verification. The completion condition is not a decorative light. It prevents the process from continuing after the stated objective has been reached.

In a structured algebra, those distinctions are not merely good habits for a careful engineer. They are candidates for the very objects and operations through which the program is expressed. That is the bridge from a finite-state diagram to a finite-state program with an intelligible form.

Here is one small fragment, stated as a program rather than as a diagram. Let `Candidate` and `Target` be distinct objects. Let `Compare(Candidate, Target)` yield one relation: lower, equal, or higher. Only `lower` permits `StepUp(Candidate)`; only `higher` permits `StepDown(Candidate)`; and only the result of one of those steps permits `Write` to the candidate store. `Write(Target)` is not an alternative spelling of the same operation. It is forbidden by the stated roles. Nor may `Write` follow directly from `Compare`: a relation is evidence, not yet a revised value. The short sequence `Compare → lower → StepUp → Write → Verify` tells another builder both what may happen and what must not be silently skipped.

At this point, it is fair to ask what makes Multenions unique among algebras. The answer cannot responsibly be: it has a remarkable name. Nor can it be: it is unique because we have declared it so. Uniqueness must be earned by a particular account of its objects, operations, constraints, and compositions. If the same account could be replaced without loss by an ordinary table of numbers, a generic flowchart, or an unstructured sequence of instructions, then its special claim has not yet been made.

This episode therefore introduces the thesis rather than pretending to settle it by assertion. Multenions proposes that there is a distinctive structured account of programmatic conduct available here. In the episodes that follow, that proposal has to acquire sharper form. We will need to state what its elementary objects are. We will need to show what operations it permits and forbids. We will need to demonstrate a composition that would be obscure if left as ordinary control flow. And we will need to build or simulate a finite example whose behavior can be checked.

That is not a retreat from the claim. It is the only way a claim about structure becomes more than an atmosphere.

There is an important practical consequence. When a program is arranged as explicit algebraic objects, failure has an address. If a controller takes an impossible transition, we can ask whether the state object was wrong, whether the event was misidentified, whether a condition was omitted, or whether an invalid composition was allowed. If the program reaches the right result for the wrong reason, we can compare the trace to the declared structure. If a new feature is proposed, we can ask which object it adds and which existing compositions it changes.

This is not a promise that an explicit system will be easy. Some of the hardest systems in engineering are hard precisely because their structure is made visible and must be kept consistent. But difficulty that can be located is different from difficulty that arrives as an unexplained output.

It also changes what it means to learn programming. A beginner is often handed a language, a syntax, and an assignment: make the computer do something. That can teach useful skills, but it can also leave the program as a string of commands whose internal form is accepted on trust. The finite-state approach begins somewhere more concrete. What states can this system occupy? What distinctions matter here? What event changes which state? What transformations are allowed? How do we know the result is valid? What trace would another person need in order to repeat the claim?

Those are algebraic questions before they are questions of a particular programming language.

They are also cybernetic questions. Cybernetics asks about control, communication, and feedback in organized systems. But control without a visible account of state can become mysticism. Feedback without an explicit relation can become a slogan. The value of a structured algebra is that it presses the vocabulary down toward the machine. It asks where the relation is held, what transformation occurs, what condition enables it, and what consequence follows.

The goal is not to make every machine small. Large systems will still exist, and some will remain trained, statistical, distributed, and difficult to compress into a handful of objects. The goal is to preserve another lineage of technical work: systems that are designed to reveal their terms of operation.

That lineage needs both a formal account and a physical home. A finite-state program cannot remain a philosophical diagram forever. Its objects must eventually be represented somewhere: in a table, in memory, in a register, in a program image, in a wire, or in a sequence of observed actions. Its operations must meet timing, power, failure, and the ordinary resistance of material systems.

For now, Multenions gives us a direction of travel. We will pursue finite-state programs as explicit algebraic objects. We will ask whether their operations can be structured so that a machine’s conduct remains visible not only after it has produced a result, but while it is being built, tested, repaired, and changed.

Next, we will make the bridge from algebra to algorithm. Naming objects and lawful operations is not yet enough: a machine also needs a stated rule for choosing its next operation, a sequence it may follow, conditions that halt it or expose an error, and a trace another person can inspect. We will specify that finite-state program before asking a real machine to carry it. Only then can the later GA144 and Forth implementation test whether this structure survives contact with hardware without losing the legibility it promised.

Thank you for listening.

## Research spine

- W. Ross Ashby, *Design for a Brain*, 2nd ed. (1960): organization, regulation, and the conditions of adaptive behavior.
- John E. Hopcroft, Rajeev Motwani, and Jeffrey D. Ullman, *Introduction to Automata Theory, Languages, and Computation*, 3rd ed. (2006): finite-state systems, transitions, and formal-language vocabulary.
- B. A. Trakhtenbrot and Ya. M. Barzdin, *Finite Automata: Behavior and Synthesis* (1973): behavior and synthesis in automata theory.
- Alexander McAulay, “Algebra after Hamilton, or Multenions” (1908), and “Multenions and Differential Invariants” I–III (1921–1923): the historical Multenions programme and its later development.

## Drafting note (not spoken)

Before recording, verify the historical wording against McAulay’s original papers and add the formal Multenions specification that defines its elementary objects, operations, and uniqueness claim. This draft introduces the historical programme and a modern finite-state exercise without inventing an equivalence between them.
