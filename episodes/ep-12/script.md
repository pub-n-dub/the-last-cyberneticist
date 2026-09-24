# Episode 12: A Machine Must Know Its Next Move

## Script

Welcome to Episode 12 of *The Last Cyberneticist*.

Last time, we separated an algebra from an algorithm. The algebra names the objects and says what operations are lawful. The algorithm says what happens next, in what order, and under which condition.

This time, we will make that distinction visible with one very small machine problem.

Imagine that a machine holds two four-bit words. One is called `Target`. It states the condition the machine is trying to reach. The other is called `Candidate`. It is the condition the machine currently has. The words may have the same binary form at some point, but they are not interchangeable. One is the demand; the other is the thing being revised.

Let the target be nine. Let the candidate begin at six.

The machine reads the candidate and compares it to the target. Six is lower than nine. That relation is evidence. It does not yet alter anything. The algorithm now gives the relation a consequence: lower permits one operation, `StepUp`.

`StepUp` produces a new candidate: seven. The machine writes seven into the candidate store. Then it verifies the write by reading the candidate again. It compares seven to nine. The result is still lower.

The same lawful cycle happens again. Step upward. Write eight. Verify. Compare eight to nine. Still lower.

Once more: step upward, write nine, verify, compare.

Now the comparator reports equality. Equality does not permit another write. It permits `Halt`. The machine has reached its stated condition, and its trace can be told in full: target nine held; candidate six read; lower; seven written and verified; lower; eight written and verified; lower; nine written and verified; equal; halt.

Nothing in this example is mysterious. That is its strength.

We can see the algebraic distinctions. Target is not candidate. Comparison is not transformation. Transformation is not storage. Storage is not verification. Equality is not merely a pleasing red lamp; it is the condition that changes what the machine is permitted to do next.

We can also see the algorithm. The algorithm is not the list of words alone. It is the rule that says: after lower, step upward; after higher, step downward; after equal, halt; after a step, write; after a write, verify; after a failed verification, enter an error condition rather than silently claiming success.

Suppose somebody skips one of those steps. They compare six with nine, see lower, and write nine directly. They may reach the desired answer, but they have not followed this algorithm. Or suppose they change the target while the candidate is being revised. The visible result may still be a number, but the trace no longer tells one stable story. Or suppose a write is attempted while the candidate store is not available. A lamp might glow. That is not enough. The program needs an error state, because the required transition has not been established.

This is why the idea matters beyond a four-bit exercise. A machine-intelligence innovation should not be judged only by whether it produces an attractive answer. We should be able to ask: what distinction did the machine hold? What relation did it recognize? What algorithm selected its next action? What state changed? What invalid action was prevented? What evidence remains for another person to inspect?

Those questions do not make a machine intelligent by decree. They establish the conditions under which its conduct can be intelligible, repairable, and answerable. Without them, an output can be impressive while the machine’s route to it remains unavailable to the people who must trust, change, or inherit it.

The little cycle also gives us a boundary. This is a controller with a defined task, not a general intelligence. It does not invent its own target. It does not decide whether adding or subtracting one is a good policy in every world. It does not learn a new rule from experience. Its value is that every one of its limits is visible.

That visibility is an existential criterion for the kind of machine work this series is pursuing. A machine has to persist through time. It has to make a difference matter to what happens next. It has to act through lawful transformations. And it has to leave enough evidence that its conduct can be reconstructed. A formal algebra helps name those conditions. An algorithm brings them into time. A physical implementation has to preserve them under the resistance of actual hardware.

The next episode takes that final step. We will ask whether the GA144 and Forth can represent this exact cycle without dissolving its distinctions into unexplained code. Which word holds each object? Which word performs each lawful transformation? How is an invalid composition prevented? And what trace lets another person tell that the machine did what we say it did?

Thank you for listening.

## Research spine

- B. A. Trakhtenbrot and Ya. M. Barzdin, *Finite Automata: Behavior and Synthesis* (1973): finite-state behaviour, specification, and synthesis.
- W. Ross Ashby, *Design for a Brain*, 2nd ed. (1960): regulation, state, and the conditions of organized behaviour.

## Drafting note (not spoken)

Before recording, decide whether the numerical demonstration will be performed manually, simulated, or illustrated with a state table. Do not imply that the GA144 implementation has already been built or verified.
