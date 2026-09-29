# Episode 12: A Machine Must Know Its Next Move

## Script

Welcome to Episode 12 of *The Last Cyberneticist*.

Last time, we separated two things that are often confused.

An algebra tells us what an operation means. An algorithm tells us when that operation happens, what permits it, what changes afterward, and how we know the account is true.

Today we will make that distinction visible without pretending that a small demonstration is already a complete multenion machine.

Begin with one bounded formal claim.

We declare two primitive units, `i1` and `i2`, in a specified basis. The relevant rules are that each squares to negative one, and that their order matters: `i1i2` is the negative of `i2i1`.

That is the algebraic contract.

Now turn it into a machine task.

The machine receives an operation request and two operands. First it validates them. Are they represented in the declared basis? Is their order known? Is there enough storage for the result? If any answer is no, the machine does not improvise an answer. It enters an error state and records the violated condition.

If validation succeeds, the machine performs exactly one named ordered product. It stores the result with its basis and grade information. Then it verifies the claim: run the reversed pair as a separate ordered operation and check that the two results have the required opposite sign. Finally, record the operands, their order, the result, the check, and the halt reason.

The result is still modest. It does not implement all of McAulay’s four-dimensional multenion system. It does not make a sixteen-component algebra appear merely because we said its name. But it does demonstrate the correct kind of bridge: a source rule, a representation, a transition, a verification, and evidence.

This is the first new insight for the listener.

A mathematical rule is not yet a machine event. The rule becomes a machine event only when the machine can represent its terms, select the operation, preserve its conditions, and leave a record that the right operation occurred.

Now return to the Four-Bit Wonder, because it teaches the same lesson with fewer symbols.

Let the machine hold two four-bit words. `Target` is the condition to be reached. `Candidate` is the condition currently held. They can have the same binary form, but they are not the same object. One is the demand; one is the value subject to revision.

Let the target be nine and the candidate be six.

The comparator reports that six is lower than nine. That relation is evidence. It does not yet write a value, move a motor, or certify success. The algorithm gives it a consequence: lower permits `StepUp`.

`StepUp` produces seven. The controller writes seven as the candidate. Then it verifies the write by reading the candidate again. The new comparison is still lower. The cycle repeats: step, write, verify, compare.

When the candidate becomes nine, the comparator reports equality. Equality does not permit another write. It permits `Halt`.

The trace is then readable: target nine held; candidate six read; lower; seven written and verified; lower; eight written and verified; lower; nine written and verified; equal; halt.

That trace is not paperwork added after the machine has finished. It is the machine’s Ariadne thread. It is how a later person can walk backward from the result to the conditions and choices that produced it. In the architectural language of Episode 4, it is the route through activities, modes, transitions, and conditions.

There is one more lesson from the labyrinth.

This target-and-candidate cycle is a fixed route. It does not search, so it does not need backtracking. But suppose a later controller must explore a bounded set of lawful transformations: perhaps several candidate rewrite rules, several sensor explanations, or several ways to reach a stated normal form.

Then it needs the labyrinth discipline.

Every complete configuration becomes a junction. Every permitted transformation becomes a corridor. An untried operation is green. An operation on the current active path is yellow. A fully explored operation is red and cannot be selected again. The machine must choose among green options by a fixed declared order. The active path is stored as predecessor links or a stack. It halts when it reaches the target, returns to the start after exhausting the finite reachable space, or reports `STEP_BOUND_REACHED` when the stated bound ends the experiment.

That last result is important.

An exhausted bound is not proof that no route exists in every imaginable extension of the system. It is evidence about this finite run, under this basis, this rule set, and this step limit. A machine earns trust not by converting every limit into a verdict, but by naming the limit and preserving the route that led there.

This lets us say something more precise about machine intelligence.

The question is not whether a machine has produced an attractive answer. The question is whether it has held distinctions stable, recognized a condition, selected a permitted operation, preserved the meaning of its representation, and left enough evidence for another person to reconstruct or challenge its conduct.

Those are strong virtues. They are also humble virtues.

The controller does not invent its own algebra. It does not prove every identity of a general multenion system. It does not decide every possible formal question. It does not become a general intelligence because it can compare, step, multiply, or search a finite graph.

Its achievement is more concrete. It can make a limited formal promise and keep it in public.

That is the criterion this series can carry forward: not an opaque result, but a legible path from condition to action to evidence.

The next episode asks how such a path can survive power-off and become durable behavior in a physical machine. Source code, a verified ROM image, an EPROM, and the board’s observed behavior will have to agree.

Thank you for listening.

## Research spine

- Alexander McAulay, “Multenions and Differential Invariants,” §§1–6: primitive units, grades, products, vectoriums, and linities.
- B. A. Trakhtenbrot, *Algorithms and Automatic Computing Machines*, Chapter 3: the labyrinth algorithm, active-path invariant, and deterministic choice convention.
- B. A. Trakhtenbrot, *Algorithms and Automatic Computing Machines*, Chapters 5–9: programs, machine configurations, transitions, and halting.

## Drafting note (not spoken)

The `i1`, `i2` operation is an illustrative finite fragment, not an implementation claim. Before recording, select an actual basis encoding, coefficient domain, product table or routine, expected results, trace format, and finite search bound. Do not claim a GA144 implementation until the words, storage map, and observed test record exist.
