# Episode 20: Toward RB5X Heiserman in a Hero-1 Body

## Script

Welcome to Episode 20 of *The Last Cyberneticist*.

The small controller has given us one honest result: a system can hold a condition, compare it with another condition, take one constrained action, and leave a trace of what it did.

That does not give us a robot mind.

It does give us a way to ask a better question about robots.

What would it take to carry a legible behavior stack into a real body?

The body in question is the Hero-1. It has its own motors, sensing limits, memory limits, power constraints, serial workflow, and mechanical history. It is not an RB5X in a different shell. It is not a historical machine waiting to be made into a copy of David Heiserman's work. Any serious continuation has to begin by respecting that difference.

Berkeley gives us one part of the vocabulary: sensing, storage, calculation, control, state, and action. Heiserman gives us another: memory, generalization, revision, and behavior that can change in relation to experience. Neither vocabulary is a drop-in program. They are questions for the repaired machine.

What can it sense?

What state can it retain?

What action can it take safely?

What observation would count as evidence that an action improved, failed, or needs revision?

Those questions lead to a modest first milestone: Beta-Hero.

Beta-Hero does not promise an autonomous creature. It establishes a repeatable embodied loop. A sensor event is read. A state is recorded. One limited motion is selected. The result is observed. The observation and the decision can be recovered through the serial workflow. If something goes wrong, the failure should be local enough to inspect rather than becoming a story about emergent behavior.

That is already difficult work. In a robot, a command is not merely a number changing in memory. Power sags. Wheels slip. Sensors misread. A mechanical part may have a history that software cannot erase. An action that was valid on a bench may be unsafe on a floor.

This is why embodiment matters. The controller has to encounter resistance from the world. That resistance is not an inconvenience added after the intelligence. It is the condition in which sensing, control, and adaptation acquire practical meaning.

Gamma-Hero is the next, still more cautious milestone. It would add a limited form of revision: not a claim that the robot has acquired open-ended learning, but a stated way for retained observations to alter a future choice within a narrow task. The rule, the stored state, the permitted adjustment, and the evidence of the adjustment all have to remain inspectable.

Here the RB5X lineage is useful as a guide rather than a blueprint. It reminds us that a robot can be organized around behavior, memory, and revision. But its particular mechanisms, assumptions, and body belong to its own machine. The Hero-1 must earn its behavior through its own sensors, actuators, and constraints.

The aim is therefore not historical cosplay and not a premature announcement of artificial intelligence. The aim is a credible embodied behavior stack: a robot that can be observed sensing, deciding within stated limits, acting, recording what happened, and being revised without becoming opaque.

That is a long road, but it is a road made of milestones rather than wishes.

The next two episodes prepare the bench for that road. Before a robot can answer back, its power, programmed memory, tools, and first interventions need to be made dependable.

Thank you for listening.

## Research spine

- Edmund C. Berkeley, *Giant Brains, or Machines That Think* (1949): sensing, memory, calculation, control, and action.
- David L. Heiserman, *Robot Intelligence* (1979): behavior, memory, and adaptive robot-programming questions.

## Drafting note (not spoken)

Name only hardware and repair milestones that have been verified on this specific Hero-1. Keep Beta-Hero and Gamma-Hero explicitly prospective until their test records exist.
