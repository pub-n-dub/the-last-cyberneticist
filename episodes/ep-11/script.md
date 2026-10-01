# Episode 11: From Algebra to Algorithm: Multenions and Program Synthesis

## Script

Welcome to Episode 11 of *The Last Cyberneticist*.

The last few episodes have been building a ladder from a very small machine.

Episode 7 asked what it means for a machine to remember. Episode 8 asked when a difference becomes consequential. Episode 9 asked what has to be true before a comparator light can count as evidence. Episode 10 introduced Multenions as a historical attempt to make objects, transformations, and invariants explicit.

Today I want to ask a question that sounds modest, but is really where a great deal of technical thinking either becomes machinery or stays a beautiful diagram on paper.

When do rules become an algorithm?

This is not the same question as whether we have a formula. It is not even the same question as whether we know the answer in a particular case. An algorithm is a promise of conduct. Given a stated kind of input, it tells us what elementary action to take, what to inspect next, when to repeat, and when to stop. It is an account of how a result comes into the world.

Boris Trakhtenbrot begins his 1963 book *Algorithms and Automatic Computing Machines* with familiar numerical work: decimal arithmetic, and then Euclid’s method for finding a greatest common divisor. That choice is useful. It prevents us from treating algorithm as a glamorous word reserved for electronic machines. A person can carry out an algorithm with pencil and paper. A calculator can carry it out without understanding the larger mathematical purpose. What matters is that the work has been decomposed into explicit, repeatable steps.

In Trakhtenbrot’s version of Euclid’s method, take two positive integers. If they are equal, stop: that common value is the answer. If they are unequal, put the larger and smaller in order, subtract the smaller from the larger, and repeat with the new pair. The number of repetitions is not known in advance. It depends on the input. But the next move is known at every stage.

That small example gives us four questions to ask of any proposed procedure. What inputs are permitted? What are the elementary operations? Which condition chooses the next operation? And what counts as completion? If any one of those answers is left as a private intuition, we may have a useful suggestion, but we do not yet have an algorithm in the strong sense.

The distinction matters at the bench. “Compare the target and the candidate, then improve the candidate” sounds like a procedure. But improve it how? Which difference is inspected? Which change is allowed? What if two changes look possible? What if the numbers are already equal? What happens if the comparison is invalid, the input is absent, or a limit is reached? The difference between a slogan and a controller lives in those questions.

Trakhtenbrot gives two names to further parts of the promise. An algorithm is general for a stated class: one finite method must work for every permitted instance, not merely the example that inspired it. And it is determinate: at each stage it must say what happens next. Generality does not mean omnipotence. It means that the domain has been named honestly. Determinacy does not mean that the result is known from the start. It means the procedure never asks its operator to supply an unrecorded act of judgment.

There is another distinction here which is almost unfashionable to say aloud. An algorithm can exist and still be practically useless at a given scale. A method can be perfectly specified, completely mechanical, and far too slow or too expensive to use. Speed is not the definition of intelligence; it is not even the definition of an algorithm. Feasibility is a separate question, one a responsible design has to ask after it has stated what it is actually doing.

That is why the word algorithm is helpful for this series. It gives us a way to resist a familiar kind of spectacle. We do not need to claim that a small controller solves every problem, or that a visible result proves a mysterious faculty. We can ask the smaller, more durable questions. What class of situation was this built for? What state can it recognize? What is it authorized to change? What record does it leave behind? And can another person follow the chain from input to action to result?

The new research on McAulay’s multenions makes the first half of this question sharper.

McAulay’s multenions are not a hidden name for an eight-part octonion machine. In the general four-dimensional case he describes an associative, noncommutative, graded algebra with sixteen scalar components. It has named primitive units, products whose order matters, grade projections, vectoriums, linear operations he calls linities, and invariant pairings.

That is valuable because it tells us what an algebra can do. It can make the terms of an operation explicit. It can say that a product is lawful. It can say that changing the order of two primitive units changes the sign. It can distinguish a scalar part from a vector part, or a grade-two component from another grade. It can name a transformation and state an identity that it preserves.

But none of those facts chooses an operation in time.

An algebra can tell us that `i1² = −1`, and that `i1i2 = −i2i1`. It cannot, by itself, tell a physical machine when two stored symbols should be treated as `i1` and `i2`, whether their order has been preserved in memory, or what should happen when an unfamiliar symbol arrives. It does not decide whether a product should be attempted, displayed, rejected, logged, or deferred. Those are algorithmic and architectural questions.

This gives us two layers, and neither can replace the other.

The first is the algebraic layer. What is this object? Which basis is it written in? Which grade does it have? What product or projection is permitted? Which relation should remain true?

The second is the algorithmic layer. Where is the object stored? What input makes an operation available? Which transition is selected? What changes in memory? What check follows? What ends the run?

An algebra without an algorithm is a map with no route. A program without an algebraic contract may run, but its important terms can remain private habits in the head of its author.

Suppose a small program says it will work with two primitive units, `i1` and `i2`. Before it performs anything, it has to declare what those names mean, where they are represented, and which rule it is testing. Now give it the request: multiply `i1` by `i2`.

The algebra tells us that the ordered product has a meaning. The algorithm still has work to do. It must validate that both operands use the declared basis. It must preserve their order. It must execute the named product. It must store the result in a layout whose grade can be identified. It must test the result against the expected relation. And it must record what happened.

If the machine instead receives `i2` followed by `i1`, it is not allowed to treat that as a harmless rearrangement. The order is part of the meaning. The program must either produce the negative result prescribed by the rule, or enter an error because its representation cannot preserve the sign. A correct-looking final lamp is not enough. The route by which that lamp was reached belongs to the claim.

Chapter 2 of Trakhtenbrot’s book gives us a second way to see why. He considers finite, two-player games with perfect information: no hidden cards, no dice, no accident smuggled in as fate. A game position can be drawn as a tree. Each vertex is a position. Each edge is a permissible move. The leaves are finished games: wins or losses.

The important distinction is between a move and a strategy. A move may look clever at the opening. A complete strategy says what to do in every situation that can arise, including positions the player hopes never to see. Working backward from the leaves, one can label a position as winning if the player whose turn it is has at least one move to a winning successor. If every permitted move hands the win to the other player, the position is losing.

This is not advice to solve chess by brute force. Trakhtenbrot explicitly separates the theoretical existence of a procedure from its practical feasibility. A finite game tree may be so vast that the procedure is useless to a person in the moment. The point is more precise: within the stated class, a complete strategy can be defined because each position is answered by the structure of the whole tree.

For our purposes, a controller is not a game opponent, but the lesson transfers cleanly. A state diagram is not yet a controller because it shows some arrows. A controller needs an answer for every reachable state. If the target matches the candidate, what follows? If it does not, what action is chosen? If a sensor value is outside the representation contract, where does the system go? If a branch is unavailable, is there another prescribed branch, an error state, or a halt? An arrow for the happy path is not a strategy for a machine.

There is a moral restraint in that. We should not call a device autonomous because it produces an output after a prepared demonstration. The serious question is whether its permitted situations have been bounded and whether its response to each one has been made legible. A small finite controller can be modest in capacity and rigorous in that respect. That is already an achievement.

The most vivid example in the book comes in Chapter 3: the labyrinth.

The labyrinth is a finite graph made of junctions and corridors. The question is not whether Theseus is inspired. It is whether a designated target junction can be reached from a designated start. Trakhtenbrot’s procedure gives the searcher a form of external memory. Corridors not yet traversed are green. Corridors traversed once are yellow. Corridors traversed twice are red.

The colors do not merely decorate the story. They are state made visible.

At a junction the procedure follows an ordered list of rules. Stop if the target has been reached. Backtrack when a loop has been closed. Otherwise take an untraversed, green corridor. Return and stop at the origin when the exploration has fully come back there. In the remaining case, backtrack along the appropriate yellow corridor. Most importantly, never enter a red corridor.

There is a beautiful invariant in this procedure. At every moment, the yellow corridors form one simple path from the start to the traveller’s present location. The yellow path is Ariadne’s thread. It says not just where the traveller is, but how this present state was reached. Since the labyrinth is finite and no corridor is used more than twice, the procedure must halt. It either reaches the target, leaving a simple route back, or it returns to the origin after exhausting the reachable territory.

That is a remarkably physical picture of memory. It is not a pile of data accumulated somewhere offstage. It is a recoverable history with a current function. The markings distinguish what is untried, what is currently active, and what has been exhausted. They prevent pointless repetition. They make a negative result meaningful: not “we failed to find the target,” but “we searched this finite, stated region under this procedure and returned with no unexplored corridor available.”

There is also a small but crucial repair in Trakhtenbrot’s account. A rule that says “take any green corridor” is not determinate. Two searchers can make different unrecorded choices. The book repairs the algorithm by requiring a fixed convention, such as choosing the first eligible corridor clockwise from the direction of entry. The convention may be arbitrary in a humane sense, but it must be fixed in an algorithmic sense.

This is exactly the kind of ordinary phrase that hides a machine’s most consequential ambiguity. “Choose an available rewrite.” “Try a nearby value.” “Select the best candidate.” “Use the next free register.” Every one of those can conceal a human choice unless an ordering rule has been declared. A tie-breaker is not bureaucratic debris. It is what turns an intention into a reproducible path.

Episode 4 gave us the architectural vocabulary of activities, modes, transitions, and conditions. Ariadne’s thread adds the missing historical dimension to that architecture. A state diagram can say what a machine may do. The thread says what it actually did, what it tried, and how it arrived here.

If a controller has only one fixed sequence—validate, multiply, verify, halt—it is not a labyrinth, and it need not pretend to be one. But if it must search a bounded set of possible transformations, rewrite paths, test branches, or fault causes, it needs an Ariadne thread of its own. It needs to know which transition remains available, which is on the active path, which branch has already been exhausted, and which fixed rule chooses among the remaining possibilities.

Otherwise a machine can arrive at an answer without leaving anyone a route back to the question.

Chapter 4 moves from the finite corridors of the labyrinth into a more dangerous territory: words and substitutions. An associative calculus begins with a finite alphabet and a finite collection of allowed replacement rules. One word may be changed into another by applying a rule at an eligible position. Two words are equivalent if a finite chain of such legal substitutions connects them.

On the surface, this can look like a game with strings. But the word problem asks a severe question: is there one method that decides, for every pair of words in a given calculus, whether they are equivalent? The associated graph is usually infinite. Every word is a vertex, and every lawful substitution is an edge. A method that simply tries substitutions can wander forever without proving that no connection exists.

Here Trakhtenbrot offers a constructive case in which the problem can be solved. The system is given directed reduction rules. Apply them in a fixed priority order, at the first eligible position. The process reduces every word to one of eight forms. The argument does not stop with the observation that the strings have changed. It proves that the reductions terminate and then uses parity invariants and an index-parity argument to show that no two of the eight reduced forms are equivalent. Two original words are equivalent exactly when their final reduced forms match.

That is the normal-form idea, and it is extremely useful at the bench. A rewrite procedure is not a decision procedure merely because it produces a tidier representation. To use a final form as evidence, we need to know that reduction ends and that the final form is meaningful enough to settle the question we asked. Termination and uniqueness—or another explicitly proved equivalence criterion—are part of the design, not decorations to add after the demo works.

The chapter’s geometric example grounds the symbols further. Letters can stand for elementary transformations of a square. Concatenating letters composes those transformations. A substitution rule can express that two different sequences have the same geometric effect. Formal marks are not empty merely because they are formal; their interpretation must be stated, and the operations on them must preserve the relation we claim they represent.

That returns us to the multenion problem. If we write a program that transforms symbolic names for algebraic objects, we must say whether it is carrying out an algebraic product, changing a storage encoding, reducing an expression to a canonical form, or merely rearranging display characters. Those are not interchangeable acts. Their output may look similar while their contracts differ completely.

This is where the series acquires a useful central claim.

For a machine to make a formal relation operational, it needs more than valid symbols and more than a working output. It needs a declared representation, a determinate transition rule, preserved invariants, an explicit completion or failure condition, and a trace sufficient to reconstruct the run.

The listener may recognize the earlier episodes in that sentence. Episode 7 said memory is not merely accumulation; it is continuity that can be recovered. Episode 8 said a difference matters only when it changes what happens next. Episode 9 said a visible signal counts as evidence only under valid conditions.

Now those ideas meet. Memory becomes the thread. A consequential difference selects a lawful branch. Evidence is the trace that lets another person walk the architectural behaviour backward.

Before calling a program multenion-informed, then, we need six promises. We need an algebraic contract: the basis, grades, operations, and identities in use. We need a representation contract: where those things live in memory or code. We need a transition contract: what makes each operation available and which fixed convention resolves a choice. We need an invariant contract: what must remain true across every permitted step. We need an evidence contract: the trace. And we need a scope contract: the limits we are not hiding.

That scope contract deserves its own sentence. A finite controller is not thereby a universal machine. A normal form that works in one stated calculus is not a solution to every word problem. A successful traversal of one bounded graph does not prove a general method for every search space. Exact claims are not modesty theatre. They are what make the work testable.

In practical terms, the trace for our small controller should be able to say: this was the input; this was the current state; this transition was chosen; this memory location or actuator changed; this check passed or failed; this was the reason for halt, error, or declared step limit. If the allowed number of steps is reached before the target or an exhaustive result, the honest output is not “no solution.” It is `STEP_BOUND_REACHED`, together with the active path and the unexplored frontier.

This does not make a program intelligent by declaration. It makes it answerable.

Next time, we will make that answerability visible in two small demonstrations. First, a declared algebraic operation will be validated, performed in order, checked, and recorded. Then the Four-Bit Wonder’s familiar target-and-candidate cycle will show how a relation becomes action only through an explicit algorithm. The concrete next action is to build the representation table and transition trace before asking the machine to persuade us of anything.

Thank you for listening.

## Research spine

- Alexander McAulay, “Multenions and Differential Invariants,” §§1–7: associative multenions, grades, vectoriums, linities, and invariants.
- B. A. Trakhtenbrot, *Algorithms and Automatic Computing Machines*, Chapters 1–4: numerical procedures, determinacy and feasibility, finite-game strategies, labyrinth invariants, and normal-form word reduction.
- B. A. Trakhtenbrot and Ya. M. Barzdin, *Finite Automata: Behavior and Synthesis* (1973): behaviour and program synthesis.

## Drafting note (not spoken)

Use only a finite, explicitly represented fragment of McAulay’s algebra in any recording demonstration. Do not identify it with octonions, claim universal computation, or claim a working GA144 realization before a representation table and test record exist. The Chapter 4 normal-form discussion refers only to Trakhtenbrot’s constructive example; do not generalize it to arbitrary associative calculi.
