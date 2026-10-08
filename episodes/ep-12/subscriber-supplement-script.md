# Episode 12 Supplement: Reading the Control Cycle

## Script

This is the companion supplement for Episode 12 of *The Last Cyberneticist*.

Thank you for subscribing and for helping to sustain the research, materials, and machine work behind this series.

The artwork gives the whole idea in one square: a fixed target, a changing candidate, a comparator, and a small sequence of lawful actions. This companion stays with the vertical control-cycle sheet and reads it slowly, one pass at a time.

The point is not that a four-bit controller is secretly a general intelligence. The point is almost the opposite. When the machine is small enough, we can see exactly what it is permitted to do, what it is not permitted to do, and what the trace of one honest run looks like.

There is a deeper question behind this little diagram. What is the difference between arriving somewhere and knowing how one arrived there? The difference is not merely archival. A final value tells us that the candidate is nine. It does not tell us whether the controller reached nine through the declared cycle, whether a write failed and was ignored, whether the target was copied into the candidate store, or whether somebody intervened between steps. A result without a route settles less than it appears to settle.

This is where Trakhtenbrot’s image of the labyrinth becomes useful. He calls it a labyrinth, following Theseus and Ariadne’s thread, though in current usage its branching junctions, loops, and alternatives make it more accurately a maze. The distinction is not pedantry. A single-path labyrinth suggests that the route is already given; a maze makes the route a question. Knowledge has to be made through choices, returns, and the careful exclusion of paths already explored.

Ariadne’s thread is therefore more than a mythic image of memory. It is a physical record of the traveller’s present epistemic condition. It says: this is the route that remains live; this is where I can return; these are the corridors whose possibilities have been exhausted. The thread does not merely preserve the past. It determines what counts as a justified next move.

Our control cycle is not itself a maze search. Its next move is fixed once the comparator gives its relation. But the same discipline is present in miniature. The trace records which state the controller was in, which relation it observed, which action was authorized, and whether the resulting write was verified. It turns a sequence of changing values into an account another person can challenge, repeat, or repair. The subscriber sheet is valuable precisely because it makes that account slow enough to inspect.

At the top of the sheet are the two registers. The target is `1001`: nine. It is fixed. The candidate is `0110`: six. It is variable. The target is not a destination written as a slogan; it is a word held in a distinct role. The candidate is not an approximate version of the target; it is the only word in this experiment that the control cycle is allowed to revise.

Both enter the comparator on separate paths. That separation is one of the quietest but most important features of the image. Before comparison, there is no reason to combine the two registers. One is the reference. One is the present value. The comparator returns a relation between them: lower, equal, or higher. It does not write either word. It does not decide the next action on its own. It reports a condition.

The first numbered step is `READ CANDIDATE`. The controller reads `0110`. It is worth pausing here because a read is not an invisible preliminary. The run begins with a claim about the actual stored word. If the controller has not read the candidate under a valid condition, everything that follows rests on an assumption rather than on a state it has observed.

Step two is `COMPARE`. The comparator sees candidate six and target nine, and returns lower. That result carries no instruction by itself. It is evidence, and the next panel tells us what the controller is allowed to infer from it.

Step three is `LOWER: STEP UP`. The candidate is incremented from `0110` to `0111`: six to seven. This is the first place where the controller changes something, but even here the new value is not yet established in the candidate register. It is the result of the permitted step, waiting to be committed.

Step four, `WRITE CANDIDATE`, records `0111` in the candidate register. The sheet is careful to call this a write, rather than quietly assuming that an arithmetic result has already become memory. In a physical machine, a computed value and a stored value are different facts. A write is the event that connects them.

Step five is `VERIFY`. The controller reads the candidate back and checks that it is indeed `0111`. If the readback did not agree, this would be the point at which the honest result is an explicit error. The controller would not keep stepping merely because its intended value was seven. It would know only that the store had failed to show the value it was required to hold.

That negative result has its own intellectual value. In a serious experiment, an error does not mean that nothing was learned. It can tell us that a particular claim has not yet been earned: perhaps the write path is unreliable, perhaps the register roles were confused, perhaps the timing assumption was wrong. The point of an explicit error state is to stop ignorance from disguising itself as completion. It keeps open the difference between “the machine did not reach the target” and “we do not yet know what happened at this transition.”

The second pass begins with a new comparison. Candidate seven is still lower than target nine. The same lawful path follows: step up to eight, write eight, verify eight. The third pass repeats it once more: step up to nine, write nine, verify nine.

Notice that repetition here is not vagueness. The controller is not “trying again” in the human sense. It is returning to a named state with an updated candidate and applying the same rule to a new configuration. The target has stayed fixed throughout. The candidate has changed one unit at a time. Every change has gone through write and verification before the next comparison.

At step fourteen, the comparator is finally presented with candidate `1001` and target `1001`. It returns equal. That is a different relation, so the algorithm permits a different transition. There is no fourth increment. There is no redundant write. At step fifteen, the cycle enters `EQUAL: HALT`.

The small red halt lamp is deliberately unspectacular. It means that the stated condition has been reached and no further action is authorized. It does not prove that the controller has discovered a goal. It proves that, for this run, a limited rule was followed to its stated completion.

The long vertical sheet is useful because it makes duration visible. In the square poster, we can understand the whole arrangement at a glance. Here we can see that the apparent simplicity of “six becomes nine” is actually a sequence of reads, comparisons, steps, writes, and checks. The result is not nine alone. The result is nine together with a path that another person can inspect.

That is the modest promise behind the artwork: visible state, lawful action, persistent memory, inspectable trace. If a later implementation is built, it will have to meet that promise in actual registers, signals, and observed tests. For now, the diagram tells us what a faithful implementation would have to preserve.

Thank you for supporting the work.

## Production note (not spoken)

Read alongside `published/artwork-control-cycle-supplement.png`. Approximate spoken length: 9–10 minutes at a reflective delivery pace.
