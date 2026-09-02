# Episode 8 Script

## Title

`A Comparator Changes Things`

## Script

Welcome to Episode 8 of `The Last Cyberneticist`.

This episode is called `A Comparator Changes Things`.

Last time, the Four-Bit Wonder taught us what it means for a machine to remember. We selected an address, wrote a four-bit value, returned to that address, and read the value back. That was already a real machine event: an address, a control state, a bus, and a stored condition meeting at the same moment.

But a remembered value by itself does not tell us very much. It is there, or it is not. The next question is whether that value stands in some relation to something else.

That is what the comparator adds.

The addition is modest: one `74LS85` four-bit magnitude comparator and three panel indications. One side receives the value currently read from the `MM2114A` SRAM. The other receives a value selected by the person using the four data switches. The result is not a sentence and not a decision. It is one of three relations.

The stored word is lower than the target.

The stored word matches the target.

Or the stored word is higher than the target.

On the panel, those relations become visible. Green says low, or increase. Red says match. Yellow says high, or decrease.

That may sound almost trivial. But it changes the character of the board. A value in memory is no longer merely displayed. It is evaluated against a condition. The machine does not yet act on that evaluation. It does not choose a target. It does not revise its own memory. It does not learn. But it now exposes a difference that could matter to a later controller.

The important discipline is to keep the signal paths honest. The comparator needs two independent words. The target comes from the switch side of the existing resistors. The remembered word comes from the read side of the SRAM bus. If both inputs were simply attached to the same bidirectional bus, the comparison would be meaningless.

The same discipline applies to time. The indication only means something while the SRAM is selected and being read. During a write, or while the memory chip is deselected, the data bus is not offering a trustworthy stored value. A lamp can be on. That does not mean the machine has told us anything useful.

This is a useful lesson beyond this small board. A visible output is not automatically evidence. We have to know what operation produced it, what state the machine was in, and whether the signals being compared were actually valid.

The demonstration is simple. Select an address. Put the machine into read mode. Set a four-bit target on the data switches. Then look at the three indicators. Change the address or the target and watch the relation change. If we make a manual write, return to read mode, and look again, we can see that the comparison changed because the stored state changed.

That makes this a small memory game. But calling it a game should not make it seem unserious. Games are often good teachers because they turn an invisible rule into a consequence that can be felt. Here the rule is a relation between a chosen value and a remembered value. The machine makes that relation public.

And there is an important limit waiting in plain sight. The same switches that provide the target are also the normal manual data-entry controls. They cannot remain a stable target while they are being used to enter a revised answer. To go further, a controller needs a captured target, a separate candidate value, and a controlled way to read, compare, step, and write.

That is not a defect in this board. It is the next question made visible.

The machine can now tell us not only what it remembers, but how that memory stands in relation to a demand.

