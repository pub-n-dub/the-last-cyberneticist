# Episode 17: Multenions Transition Automation in GA144

## Script

Welcome to Episode 17 of *The Last Cyberneticist*.

The last few episodes separated a difficult claim into small parts. A machine can hold a state. It can compare that state with a condition. It can apply one permitted transformation. It can verify the result. And it can halt or report an error instead of silently inventing a success.

That was the point of the small four-bit cycle: `Compare → StepUp or StepDown → Write → Verify`.

Today the question is whether that organization survives when it becomes a program on a real machine.

The machine is the GA144. The language is Forth. But neither name should be allowed to do the explanatory work for us. A processor and a programming language do not make an intelligible controller merely by being present. We still need to say what is represented, what operation is permitted, what state follows, and how another person can inspect the result.

So begin with the objects, not the code.

There is a `Target`: the condition the system is trying to reach. There is a `Candidate`: the condition it currently holds. There is a `Relation`, produced by comparison: lower, equal, or higher. There is a `Trace`: a record sufficient to show which lawful transition occurred. And there are error conditions: no target, an invalid state, a failed write, or a transition for which no rule has been defined.

In Forth, these distinctions can be made concrete as named words and named storage. A word that fetches `Candidate` is not a word that fetches `Target`. A word that compares them is not a word that writes memory. A word that performs `StepUp` is not available because a number happens to be on a stack; it is reached because the current relation permits that transition.

This is the practical meaning of explicit organization.

Suppose the candidate is six and the target is nine. The comparison word reports `LOW`. The transition rule selects `StepUp`. `StepUp` produces seven. A write word stores seven as the new candidate. A verification word reads it back. The trace records the relation, transformation, and result. Then the cycle begins again.

If the relation is `HIGH`, the permitted transformation is different: `StepDown`. If it is `EQUAL`, neither step word is lawful. The only normal next move is `Halt`.

The machine is not made more intelligent by giving those words impressive names. Its value lies elsewhere: the distinctions that govern its conduct are available for inspection. We can identify where the target is held, where the candidate is held, which word compares them, which words alter state, and which condition prevents another alteration.

Time matters here because the program is not just a static diagram. It is an ordered succession. Read. Compare. Select. Transform. Write. Verify. Halt or continue. Each stage changes what can lawfully happen after it. A trace makes that order recoverable.

That also lets failure remain local. If a candidate was not written, verification should not report success. If a relation has no matching transition, the controller should enter an error state rather than choosing an action by accident. If a value is outside the stated representation, that fact belongs in the record. An unexplained output is not evidence of a mysterious intelligence; it is a question left unanswered.

This is what the GA144 implementation is meant to test. Not whether Forth can make a clever demo. It can. The test is whether the structured program remains visible at the level of the machine: objects represented as storage, transformations represented as words, restrictions represented as control paths, and conduct represented as a trace.

The result, if it works, is still a finite-state controller. It does not discover its own goals. It does not generalize beyond the task we give it. It does not become a general intelligence because it can move a candidate toward a target.

But it does meet a more modest and useful standard. It lets us see how a program persists through time as a lawful organization of state, memory, transformation, constraint, and evidence.

That is enough to make the next question concrete.

What happens when the same small cycle is no longer only represented in software, but embodied as its own slow, visible hardware controller?

Thank you for listening.

## Research spine

- Alexander McAulay, *Algebra after Hamilton, or Multenions* (1908): the historical prompt for named objects, operations, and compositions.
- B. A. Trakhtenbrot and Ya. M. Barzdin, *Finite Automata: Behavior and Synthesis* (1973): finite-state behaviour and traceable synthesis.

## Drafting note (not spoken)

Before recording, verify the actual GA144 word names, storage locations, target hardware, and trace mechanism. Do not claim a working implementation until it has been built and tested.
