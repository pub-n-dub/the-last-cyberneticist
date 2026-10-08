# Episode 12: A Machine Must Know Its Next Move

## Script

Welcome to Episode 12 of *The Last Cyberneticist*.

There is a particular mistake that becomes easy to make when a formal system is beautiful. We see a compact rule, an elegant identity, or a suggestive diagram, and begin to speak as though the machine has already done something merely because the rule can be stated.

It has not.

A mathematical relation can be perfectly sound and still have no time, no memory, no input convention, no failure condition, and no material consequence. It becomes part of a machine only when somebody decides how its terms will be represented, what event calls for it, which operation is permitted, and what record remains when the operation is over.

That is the question for this episode: what must be present before a machine can honestly be said to know its next move?

The answer is not consciousness. It is not a claim that the machine has grasped the purpose of its work in the way a person might. It is more exact, and more useful. The machine needs a complete enough account of its present condition that one permitted next action can be selected without an unrecorded human judgment.

The artwork for this episode puts the whole claim in one field of view. At the top are two small registers. One is `TARGET`, fixed at `1001`: nine. The other is `CANDIDATE`, beginning at `0110`: six. Between them sits a comparator. Below them is the complete sequence: read candidate, compare, step up when lower, write candidate, verify, and halt when equal. It is not an image of a mysterious intelligence. It is an instrument panel for a limited machine whose conduct can be followed.

The side panels are as important as the central cycle. One says, “two words, two roles.” Another marks two tempting arrows as not permitted: comparison may not jump straight to writing, and the target may not be written into the candidate store. A third gives failed verification its own explicit error state. These are not decorative cautions. They are the difference between a sequence of values and a controller with a claim to make.

Begin with a deliberately small formal claim.

We declare two primitive units, `i1` and `i2`, in a stated finite basis. Each squares to negative one. Their order matters: `i1i2` is the negative of `i2i1`. This is only a fragment chosen for an experiment. It is not a claim to have implemented McAulay’s complete four-dimensional multenion system, and it should not be inflated into one.

Even so, the fragment has obligations. The symbols must mean something stable. The machine cannot quietly treat `i1` as an arbitrary character one moment and as an algebraic unit the next. Nor can it receive `i2`, `i1` and rearrange them into `i1`, `i2` because that happens to be more convenient for a table lookup. In this little universe, order belongs to the meaning.

We can now distinguish five things that are too often compressed into the phrase “do the multiplication.” There is the request. There is the representation of each operand. There is the selected operation. There is the stored result. And there is the test that tells us whether the stated rule was kept. A working machine has to keep those things apart long enough for them to be checked.

Imagine a request record with fields for operation, left operand, right operand, and run identifier. The operation field might say `ORDERED_PRODUCT`. The operands might say `i1` and `i2`. The run identifier is not algebra; it is there so that a later trace can tell this attempt from another one. A representation table then says which stored code stands for each permitted primitive unit, which codes are invalid, and where sign and grade are placed in a result.

The particular codes are not sacred. We might use small integers, bit patterns, tagged records, or names in a simple interpreter. What matters is that the choice is declared before the result is admired. If code `01` means `i1` today and means a sign bit tomorrow, the experiment has lost the continuity it needs to make a claim.

Validation is the machine’s first real move. Is the requested operation one that this bounded experiment supplies? Are both operand codes present in the declared table? Are they in the required order slots? Is the output location available? Is the coefficient or sign representation sufficient for the result? A failure at this stage is not an embarrassment to conceal. It is a result of a different kind: `INVALID_OPERAND`, `UNSUPPORTED_OPERATION`, or `STORAGE_UNAVAILABLE`, with the relevant condition recorded.

This may sound excessively cautious for two symbols and a small table. But the smallness is what lets us see the principle. A great many large systems rely on precisely these checks while hiding them behind friendly interfaces. The interface says “calculate.” The actual machine has to decide whether the input parses, whether the types agree, whether the address is valid, whether an arithmetic exception occurred, and whether a result can be committed. A small controller has fewer cases, not fewer responsibilities.

Suppose validation succeeds for `ORDERED_PRODUCT(i1, i2)`. Now the controller may enter an execution state. It selects the row and column corresponding to the two operand codes, reads the stored product, and writes a result record. The result must preserve more than a pleasing display string. It needs a basis label, a sign, and whatever grade information the stated representation makes relevant. If the result is later displayed as a named composite unit, that display name is an interpretation of the stored record, not a substitute for it.

Then comes verification. The controller runs the reversed request as a separate event: `ORDERED_PRODUCT(i2, i1)`. It does not merely negate the first answer and congratulate itself. It performs the second lookup under the same representation contract. Only then does it check whether the two result records agree in basis and differ in sign as the rule requires. The trace can therefore say which two operations occurred, in what order, what they returned, and which comparison passed or failed.

There is a valuable restraint here. Verification is not an oracle. If the product table and the checker were copied from the same mistaken assumption, they can agree while both are wrong. A responsible experiment should therefore identify an independent source for expected cases: a hand-checked table, a separately reviewed derivation, or a second implementation whose errors are not likely to be identical. The trace shows that this implementation was internally consistent. It does not by itself prove every premise from which the implementation was made.

That distinction keeps the word evidence honest. Evidence is not a light that comes on at the end of a program. It is a documented connection between a claim, the conditions under which the claim was tested, the transitions that occurred, and the observed outcome.

The Four-Bit Wonder lets us see the same structure without algebraic notation.

Let it hold two four-bit words, `Target` and `Candidate`. They may contain the same binary pattern on a particular run, but they have different roles. `Target` is the condition that has been set. `Candidate` is the value that the controller is authorized to revise. Confusing the two would make a successful-looking demonstration meaningless: a controller could simply overwrite the demand rather than bring the candidate into relation with it.

Take a target of nine and a candidate of six. The first state is not “increase.” It is `READ`. The controller reads both stored words under a stated valid-read condition. It then enters `COMPARE`, where the comparator returns one of three relations: lower, equal, or higher. That relation is evidence about the present configuration. It is not yet an instruction to a register.

Only the transition rule gives the relation a consequence. If the candidate is lower, `StepUp` is permitted. If it is higher, `StepDown` is permitted. If it is equal, `Halt` is permitted. No other transition is available in those states. In particular, equality does not permit another increment merely because the controller has been moving upward, and a lower result does not permit a write to the target store.

It is useful to be precise about what “present configuration” means. It is not simply the number that happens to be visible on a display. For this controller, a configuration includes at least the target word, the candidate word, the current activity, the most recent relation, and the status of the last write verification. Two runs can show the same candidate value and still be different configurations. A candidate of nine immediately after a verified write is not the same as a candidate of nine read from an uncertain location, or one that appears while the controller is still in the middle of a transaction.

That is why a state name is not decorative. `COMPARE` says which question the machine is currently authorized to ask. `WRITE_CANDIDATE` says which memory location may change. `VERIFY_WRITE` says that the controller is not yet entitled to treat the intended change as an accomplished fact. A well-made transition table narrows authority at every point. It tells us not just what the machine can do, but what it is forbidden to do while this particular distinction is unsettled.

The same discipline clarifies timing. If the candidate is read, compared, and later written, a physical implementation has to specify whether anything else may alter the store in between. If it may, the comparison can become stale before the write occurs. In a simple bench experiment we can prohibit that by giving the controller exclusive control for one cycle. In a larger system we may need a lock, a version number, or a fresh comparison before committing the result. The specific mechanism changes; the requirement does not. An action should be licensed by conditions that are still true when the action is taken.

This is one reason a trace should record transition identifiers, not only values. A list that says “six, seven, eight, nine” tells us that values changed. It does not tell us whether each change followed a lower comparison, whether the write was verified, or whether someone bypassed the controller altogether. A compact record such as `COMPARE:LOWER → STEP_UP → WRITE_CANDIDATE → VERIFY_OK` carries much more of the machine’s conduct without pretending to preserve every electrical detail.

For the run at hand, lower selects `StepUp`. Six becomes seven in a working register. The controller enters `WRITE_CANDIDATE`, commits seven to the candidate store, and then enters `VERIFY_WRITE`. It reads the candidate again and checks that the stored value is seven, not merely that a write signal was issued. Only after that verification does it return to `COMPARE`.

The next two cycles have the same form. Seven is lower than nine; eight is written and verified. Eight is lower than nine; nine is written and verified. At that point the comparator reports equality. Equality selects `HALT`. The final trace can be read as a sequence of accountable claims: target nine read; candidate six read; lower; seven produced; seven written; seven read back; lower; eight produced; eight written; eight read back; lower; nine produced; nine written; nine read back; equal; halt.

Notice what is absent from that account. There is no appeal to a vague instruction to “get closer.” Closeness might be useful language for a designer, but it is not yet a rule a controller can execute. The actual controller needs named relations, named actions, a place to store the revised value, and a condition under which it stops. A machine does not need a grand philosophy to know its next move. It needs its present distinctions made operational.

The boundary cases teach this even more sharply. What happens when a four-bit candidate is already fifteen and a command would step it upward? What happens if the target is absent, a read returns an invalid word, a write cannot be verified, or the candidate has been changed by some other process between comparison and write? A persuasive state diagram cannot omit these cases and call itself complete.

For a bounded experiment, we can make the scope explicit. Inputs are the sixteen valid four-bit words. The controller may require exclusive control of the candidate store during a cycle. Attempting `StepUp` at fifteen enters `UPPER_BOUND`, rather than silently wrapping around to zero. Attempting `StepDown` at zero enters `LOWER_BOUND`. A failed readback enters `WRITE_UNVERIFIED`. An invalid input enters `INVALID_WORD`. Each state has a defined halt, recovery, or error transition. The machine may still be simple, but it is no longer relying on the operator to repair its specification halfway through a run.

This is why a trace matters. It is not a diary composed after the fact. It is state made available to later inspection. The trace preserves the distinction between a controller that reached nine by lawful increments and a controller that happened to display nine after a memory fault, an operator intervention, or an unauthorized write. The visible result alone cannot tell us which history occurred.

There are several ways to keep such a trace. A tiny machine may expose state lights, a serial line, a paper log, or a sequence of manually copied registers. A larger one may keep timestamped records with transition identifiers and checksums. The appropriate mechanism depends on the machine. The invariant is the important thing: the record must be sufficient for another person to reconstruct the relevant path without asking the original operator to remember what happened.

That phrase, relevant path, matters when a controller has choices.

The target-and-candidate routine follows one fixed route. It compares, steps, writes, verifies, and compares again. It is not a search. But many systems eventually must choose among several lawful operations: a repair controller may test several fault hypotheses; a rewrite system may have several eligible rules; a planner may have several bounded actions available from one configuration.

Here the labyrinth offers a demanding model. Treat each complete configuration as a junction and each permitted action as a corridor. An action that has not been tried is green. One on the active path is yellow. One whose possible consequences have been fully explored is red. The controller stores predecessor links or a stack, so the active path is recoverable rather than imaginary. It selects among green actions with a fixed priority order, not with the phrase “choose whichever seems best.”

That fixed order can be arbitrary and still be essential. Perhaps operations are attempted alphabetically by their identifier, perhaps in a physical clockwise order, perhaps by a declared numeric priority. The choice does not become objectively profound just because it is written down. Its virtue is reproducibility. Two operators given the same configuration and the same rule will traverse the same finite path, and a later investigator can tell why one corridor was taken before another.

The colors also protect the meaning of failure. If a finite reachable space has been exhausted under a fixed transition set, the machine can report `NO_ROUTE_IN_STATED_SPACE`. If a declared experiment permits only one thousand transitions and reaches that bound first, it reports `STEP_BOUND_REACHED`. Those are different results. The former concerns exhaustive exploration of the stated finite space. The latter says only that the experiment ended while possibilities remained. Neither sentence should be converted into a grand claim about every extension of the formal system.

This is where the idea of intelligence can become needlessly theatrical. A machine that can preserve roles, recognize a condition, select a permitted operation, verify a change, and expose its trace is not thereby a general reasoner. It has not escaped its specification. But neither is it trivial in the dismissive sense. It has made a limited formal promise and kept that promise in public.

That is a stronger standard than an attractive output. An attractive output can be accidental, staged, or detached from the process that produced it. A legible path binds an output to its conditions. It lets a builder find a mistake, lets a maintainer repeat a test, and lets a critic say exactly which assumption must be challenged.

Return for a moment to the image of the two registers. The target does not travel through the machine as a command to be copied. It remains a reference. The candidate is the thing that travels: from readout, to comparison, to a permitted step, to a write, to verification, and back to comparison. That movement is modest, but it contains the whole moral of the episode. A condition may guide an action without being confused with the thing acted upon.

The halt lamp at the end is deliberately restrained. It does not announce a triumph of artificial intelligence. It says only that the candidate has reached the stated target under the declared cycle. If verification had failed, the honest lamp would be `ERROR`, not a forced continuation toward a pleasing result. If the candidate had already equalled the target, the honest action would have been to halt without writing. A machine becomes more trustworthy when it can decline an unauthorized action as clearly as it can perform an authorized one.

This is what the poster means by a bounded controller. Its state is visible. Its actions are lawful. Its memory has named roles. Its trace can be inspected. The bounds do not diminish the experiment; they give it a definite shape. We can say what was tested, what was not tested, and what a correct result actually establishes. That is a far better foundation for further work than a system that asks us to infer its discipline from a final display.

So a machine knows its next move when the relevant distinctions have been given a durable form: what it is holding, what it has observed, what transitions are permitted, what condition selects among them, and what will count as success, error, or a justified limit. The machine need not know why we care about the answer. We do. Our responsibility is to ensure that its conduct does not depend on a hidden decision that only appears after something has gone wrong.

That is the practical discipline at the heart of this series. Keep the claim bounded. Name the representation. State the transition. Check the result. Preserve the route.

Thank you for listening.

## Research spine

- Alexander McAulay, “Multenions and Differential Invariants,” §§1–6: primitive units, grades, products, vectoriums, and linities.
- B. A. Trakhtenbrot, *Algorithms and Automatic Computing Machines*, Chapters 1–4: determinacy, finite-game strategies, the labyrinth algorithm, active-path invariants, and fixed choice conventions.
- B. A. Trakhtenbrot, *Algorithms and Automatic Computing Machines*, Chapters 5–9: programs, machine configurations, transitions, and halting.
- B. A. Trakhtenbrot and Ya. M. Barzdin, *Finite Automata: Behavior and Synthesis* (1973): behavioural descriptions and synthesis.

## Drafting note (not spoken)

The `i1`, `i2` operation remains an illustrative finite fragment, not an implementation claim. Before recording, select an actual basis encoding, coefficient domain, product table or routine, expected results from an independently checked source, trace format, and finite search bound. Do not claim a GA144 implementation until the words, storage map, and observed test record exist.
