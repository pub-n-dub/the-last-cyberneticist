# Episode 11: From Algebra to Algorithm: Multenions and Program Synthesis

## Script

Welcome to Episode 11 of *The Last Cyberneticist*.

In the previous episode, I introduced Multenions as a structured algebra: a way of insisting that a program name its objects, operations, relations, and lawful compositions. That gives us a discipline. It does not yet give us a machine that knows what to do next.

That missing thing is an algorithm.

An algebra can tell us that `Candidate` and `Target` are different kinds of object. It can tell us that comparison yields one of three relations: lower, equal, or higher. It can tell us that writing a target into a candidate store is not the same operation as writing a revised candidate. It can forbid a write that has no valid source.

But none of that alone chooses the next move. When the candidate is lower than the target, should the machine add one, add two, ask for another input, stop, or report an error? An algebra makes those alternatives distinguishable. An algorithm selects one and gives the selection an order in time.

That distinction is not a technical footnote. It is one of the criteria by which a claim about machine intelligence becomes serious. A result is not enough. A vocabulary of states is not enough. A machine must have a stated way to encounter a condition, select a lawful action, preserve or alter its state, and determine whether it has completed or failed its task.

For this series, we can begin with a deliberately small program. There are two held words: `Target` and `Candidate`. There is a relation produced by `Compare(Candidate, Target)`. There are three possible results: lower, equal, and higher. There are three possible responses: `StepUp`, `Halt`, and `StepDown`.

Now the algorithm can be stated plainly.

First, hold the target stable. Then read the candidate. Compare the candidate to the target. If it is lower, produce a candidate one step higher. If it is higher, produce a candidate one step lower. If it is equal, halt. After a step, write the revised candidate. Then read and compare again. The process ends only when equality is verified, or when an error condition says that a required operation could not be completed.

The order matters. `Compare` is evidence; it is not a write. `StepUp` is a transformation; it is not proof that storage changed. `Write` is a state change; it is not proof that the right value was written. `Verify` is what returns us to evidence.

That gives us a finite-state algorithm. It has states such as capture target, read candidate, compare, step upward, step downward, write, verify, halt, and error. It has inputs and conditions. It has permitted transitions. It has transitions that are forbidden. And it has a trace that another person can inspect.

This is where the language of finite automata becomes useful. Trakhtenbrot and Barzdin distinguish the observable behaviour of an automaton from the synthesis of its program. The first asks what the machine does. The second asks what organized structure must be constructed so that it can do it. We need both questions. A flashing light, or even a correct final word, tells us very little unless we can say which state was entered, which condition was recognized, which transition was permitted, and how the next state was produced.

The bridge to Multenions must therefore be explicit. We are not entitled to call this little controller McAulay’s formal system merely because it has named objects. The historical correspondence has to be specified and tested. But we can use this program to state the engineering question clearly: what representation, operation, and composition would make the algebra visible in a real program rather than leaving it as a description applied afterward?

Before we choose a machine or a programming language, we need a minimal specification. It should name the object types. It should state the relation returned by comparison. It should say which relation enables each transformation. It should prevent a target from being written accidentally as a candidate. It should state what evidence counts as a successful write. And it should describe halt and error conditions as part of the program, not as failures of imagination outside it.

Only after that specification exists can an implementation be judged. Forth, the GA144, a table-driven controller, or a wire-wrapped sequencer may all be possible representations. None is the algorithm simply because it can run instructions. The implementation has to preserve the distinctions and transition rules that the algorithm requires.

Next time, we will walk through this small program as a complete cycle. We will hold a target, begin with a candidate, follow each comparison and revision, and ask what a trace lets us know. The aim is not to make a grand intelligence claim. It is to see the minimum condition under which a machine can be said to know its next move in a way that remains visible to us.

Thank you for listening.

## Research spine

- B. A. Trakhtenbrot and Ya. M. Barzdin, *Finite Automata: Behavior and Synthesis* (1973): the distinction between observable automaton behaviour and program synthesis.
- Alexander McAulay, “Algebra after Hamilton, or Multenions” (1908): historical source requiring further formal verification before a direct implementation claim is made.

## Drafting note (not spoken)

Before recording, replace any informal description of Multenions’ formal objects with verified definitions from McAulay’s original work or clearly mark it as the series’ modern finite-state exercise.
