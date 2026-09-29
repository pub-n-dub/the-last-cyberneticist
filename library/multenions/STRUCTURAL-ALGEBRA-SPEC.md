# Structural Algebra SA-8: formal, PolyForth, and silicon specification

## Status and intent

**Structural algebra** is a proposed engineering term here, not a standard name
for a separate branch of algebra.  It means an algebra whose full multiplication
law is finite, explicit, table-addressable, and therefore has the same source of
truth in a proof, a Forth program, and a hardware description.

`SA-8` is the octonion specialization of that idea.  It reconciles the material in
`OCTONIONS-KNOWLEDGE-AGENT.md` with implementable constraints: octonion products
are valid as atomic binary operations; a chain of products must carry its chosen
parenthesization.

## 1. Formal definition

Let `C` be a commutative ring with identity.  Define

```text
SA-8(C) = { a0 e0 + a1 e1 + ... + a7 e7 | ai ∈ C }
```

where `e0 = 1` and the product is extended `C`-bilinearly from the basis table
below.  Addition and additive inverse are componentwise.  `e0` is the two-sided
multiplicative identity.

For basis indices `i,j ∈ {0,...,7}`, define a signed product map

```text
P(i,j) = (sign, k),  sign ∈ {+1,-1}, k ∈ {0,...,7}
ei ej = sign · ek.
```

Then, for `x = Σ ai ei` and `y = Σ bj ej`, the **only primitive product** is

```text
x ⊙ y = Σi Σj ai bj · P(i,j).
```

Here `ai bj · (+1,ek)` means add `ai bj` to output component `k`; with `-1`,
subtract it.  This equation is both the formal semantics and the reference
implementation algorithm.

### Required identities

Define the involution and norm by

```text
x̄ = a0 e0 - Σ(i=1..7) ai ei
N(x) = x x̄ = (Σ(i=0..7) ai²)e0.
```

`SA-8(C)` is the Cayley/octonion composition algebra over `C`: it is unital,
noncommutative, nonassociative, alternative, and satisfies the Moufang
identities.  It has `N(x⊙y) = N(x)N(y)`.  A nonzero element can be treated as
invertible only when `N(x)` is a unit of `C`; then `x⁻¹ = x̄/N(x)`.

The inverse guarantee therefore applies over `R` and `Q` for nonzero `x`, but it
does **not** generally apply in a modular machine ring such as `Z/(2^W)Z`.

### Normative basis-product table

Table entry `-3` means `-e3`; `+0` means `e0`.  This orientation agrees with
Taylor's basis `e1,e2,e3,f0,f1,f2,f3` under
`(e4,e5,e6,e7) = (f0,f1,f2,f3)`.

| `ei ⊙ ej` | `e0` | `e1` | `e2` | `e3` | `e4` | `e5` | `e6` | `e7` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `e0` | +0 | +1 | +2 | +3 | +4 | +5 | +6 | +7 |
| `e1` | +1 | -0 | +3 | -2 | +5 | -4 | -7 | +6 |
| `e2` | +2 | -3 | -0 | +1 | +6 | +7 | -4 | -5 |
| `e3` | +3 | +2 | -1 | -0 | +7 | -6 | +5 | -4 |
| `e4` | +4 | -5 | -6 | -7 | -0 | +1 | +2 | +3 |
| `e5` | +5 | +4 | -7 | +6 | -1 | -0 | -3 | +2 |
| `e6` | +6 | +7 | +4 | -5 | -2 | +3 | -0 | -1 |
| `e7` | +7 | -6 | +5 | +4 | -3 | -2 | +1 | -0 |

Equivalent oriented Fano triples are
`(1,2,3) (1,4,5) (2,4,6) (3,4,7) (1,7,6) (2,5,7) (3,6,5)`.
For every cyclic triple `(i,j,k)`, `ei ej = ek`; reversing operands negates the
answer.  This is a convenient compact check on any copied table.

## 2. Semantic contract for all implementations

```text
oct_mul(x,y)       = x ⊙ y                    (atomic binary operation)
oct_left3(x,y,z)   = oct_mul(oct_mul(x,y),z)  ((x⊙y)⊙z)
oct_right3(x,y,z)  = oct_mul(x,oct_mul(y,z))  (x⊙(y⊙z))
```

`oct_left3` and `oct_right3` are intentionally distinct interfaces.  A compiler,
Forth definition, netlist optimizer, or CAD schematic must not replace one with
the other.  Scalar arithmetic *inside* the fixed `oct_mul` reduction may be
balanced or pipelined, because additions and multiplications in `C` are
associative; it must not change the 64 signed terms or their destination lanes.

## 3. PolyForth realization

### Data representation

- An octonion occupies eight consecutive signed cells in canonical order
  `[a0 a1 a2 a3 a4 a5 a6 a7]`.
- For exact machine algebra choose `C = Z/(2^W)Z`: permit deliberate cell-width
  wraparound on every scalar add/subtract/multiply.
- For integer mathematics without wraparound, use double-cell products (`M*`) and
  a wider accumulator for each lane.  Convert or signal overflow explicitly.
- Fixed-point (`Qm.n`) is useful for approximations but is not algebraically
  exact after per-operation rounding.  Round only at the API boundary if the
  identities are to be tested internally.

### Portable implementation shape

Use two 64-byte ROM/table arrays, indexed by `8*i+j`:

```text
DEST[8*i+j] : 0..7          \ basis-output lane k
NEG [8*i+j] : 0 or 1        \ subtract product if 1
```

Pseudocode deliberately uses only ordinary Forth concepts; rename stack and
memory words to the local PolyForth dialect.

```forth
\ ( x-addr y-addr out-addr -- )
: OCT-MUL
  8 0 DO  0 out-addr I CELLS + !  LOOP
  8 0 DO
    8 0 DO
      x-addr I CELLS + @  y-addr J CELLS + @  M*   \ signed scalar product
      I 8 * J + DUP DEST + C@                     \ product, table-index, lane
      out-addr SWAP CELLS +                         \ product, result-lane-addr
      SWAP NEG + C@ IF DNEGATE THEN                 \ adapt DNEGATE for M* result
      ROT D+!                                       \ wide accumulate into lane
    LOOP
  LOOP ;
```

This is semantic pseudocode, not drop-in PolyForth source: the exact double-cell
accumulator words and return-stack idioms vary by target.  The implementation
must populate `DEST` and `NEG` directly from the normative table, rather than
hard-code an unverified set of Fano-plane arrows.

Minimum test vectors:

```text
e1⊙e2 =  e3       e2⊙e1 = -e3       e1⊙e1 = -e0
e1⊙e6 = -e7       e6⊙e1 =  e7       e5⊙e6 = -e3
(e1⊙e2)⊙e4 =  e7  e1⊙(e2⊙e4) = -e7
x⊙x̄ = (Σ ai²)e0  for representative integer vectors x
```

The fourth vector is a mandatory nonassociativity regression test.

## 4. Silicon-CAD block definition

### RTL/schematic boundary

```text
Module: sa8_mul
Parameters: W (coefficient width), ARITH_MODE {MODULAR, WIDE, FIXED_POINT}
Inputs:  x[0:7], y[0:7]  -- signed W-bit two's-complement coefficients
Outputs: z[0:7]          -- signed result coefficients; width is mode-specific
Control: clk, rst_n, valid_in, ready_in / valid_out, ready_out (if pipelined)
Semantics: z = x ⊙ y according to the normative basis-product table
```

`MODULAR` is the simplest fully exact hardware interpretation: output lanes have
width `W` and retain the low `W` bits of scalar arithmetic.  `WIDE` should expose
at least `2W+6` signed bits per output lane before any external narrowing: one
lane is a signed sum of up to 64 products, so six guard bits cover worst-case
addition growth.  `FIXED_POINT` must name its binary-point position and rounding
rule in the module parameters; it implements an approximation, not the exact
ring algebra.

### Datapath architecture

1. Fan out the eight `x` and eight `y` coefficients.
2. Form the 64 signed scalar products `p(i,j) = x[i] * y[j]`.
3. Route each product to `z[DEST(i,j)]`, through a sign inverter when
   `NEG(i,j)=1`.
4. Sum each of the eight routed groups with a balanced adder tree.
5. Register the multiplier and/or adder-tree stages as dictated by clock target.

The 8×8 sign/destination map is constant wiring; no runtime table RAM or
microcode is needed.  A resource-reduced sequential version may reuse one scalar
multiplier and perform the same 64 accumulate operations over 64 cycles.  Both
implementations conform if they have the same arithmetic mode and output value.

### CAD-facing invariants and verification

- Preserve the coefficient order and the exact table as parameters locked in the
  design review package.
- Use signed multiplication and signed extension at every adder-tree input.
- Treat `sa8_mul` as a nonassociative operator in high-level synthesis: chained
  expressions require explicit intermediate nets.
- Property tests, for values safe from overflow, should prove identity, conjugate
  reversal, alternativity `x⊙(x⊙y)=(x⊙x)⊙y`, and norm composition.
- Equivalence-test the RTL against a 64-term reference model generated from this
  table, plus the nonassociativity vector above.

## 5. Design decision to make before implementation

Choose the coefficient ring at the system boundary:

| Requirement | Recommended `C` / mode | Consequence |
| --- | --- | --- |
| Bit-exact deterministic hardware transform | `Z/(2^W)Z` / `MODULAR` | Exact finite algebra, but nonzero values need not be invertible. |
| Exact integer or rational calculation | widened integers / software big integers | Preserve arithmetic, with explicit growth and throughput cost. |
| DSP or geometry approximation | signed fixed point / `FIXED_POINT` | Efficient, but rounding invalidates exact identities. |
| Field-like inverse and Euclidean norm | real/float software model | Matches the familiar real octonions; hardware division is separate. |

No one choice is universally correct.  The algebraic structure is fixed by the
table; the coefficient ring determines whether the system is exact, invertible,
bounded, or approximate.

## 6. Integration notes

- **Canonical interchange form:** serialize a value as eight signed coefficients
  in increasing basis order, `a0..a7`.  Include the arithmetic mode, coefficient
  width, binary-point position (when applicable), and this table's orientation in
  any packet, register map, or saved vector set.  A bare eight-word vector is
  otherwise ambiguous across octonion conventions.
- **Associator as a diagnostic port:** when debugging or characterizing a design,
  expose `assoc(x,y,z) = (x⊙y)⊙z - x⊙(y⊙z)`.  It must be zero for any triple
  lying in one common two-generator subalgebra, but it is intentionally nonzero
  in general.  This makes accidental reassociation visible rather than silent.
- **Latency is part of the interface:** a pipelined `sa8_mul` should publish a
  fixed `LATENCY` parameter and preserve operand/result transaction ordering.
  Parentheses must be represented by actual intermediate transactions or nets;
  a generic multiply-chain scheduler is not permitted to reshape them.
- **Table is configuration, not tuning:** revisions to the product table change
  the algebra.  Store the table alongside firmware, RTL, test vectors, and CAD
  symbols as a versioned design input, and require equivalence tests whenever it
  changes.
