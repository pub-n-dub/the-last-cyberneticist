# Knowledge notes: McAulay’s *Multenions and Differential Invariants*

## Source and scope

**Source parsed:** [Multenions-and-Differential-Invariants.pdf](Multenions-and-Differential-Invariants.pdf), Alexander McAulay, 69 pages.

This note is based only on that PDF. It is a structured paraphrase and index of McAulay’s terminology, algebraic construction, and intended differential-geometric applications; it is not a transcription.

The paper presents a general associative algebra of “multenions,” then builds a calculus of linear operators, rotations, vectoriums, invariants, covariants, differentiation, curvature, relativity, electromagnetism, and stationary action. It includes later corrections and additions dated within the text to 1921–22. The paper’s historical physics language and notation should therefore be treated as period material, not as a current formulation of relativity or field theory.

## The central idea

McAulay wants a single algebraic language in which quantities of different geometric grades—scalars, vectors, bivectors, and higher-grade objects—can be multiplied, projected, transformed, differentiated, and made invariant.

The architecture is:

```text
n anticommuting unit vectors
  → products of distinct generators (“primitive vectoriums”)
  → a 2^n-dimensional graded multenion algebra
  → grade-selecting and reversal/sign-changing linities
  → vectoriums and their normal reciprocals
  → extensions of vector transformations to every grade
  → invariant differential and geometric constructions
```

The paper treats multenions as a generalization and reorganization of quaternion methods, especially for higher-dimensional geometry and differential invariants.

## The foundational algebra (§1)

### Laws I–IV

McAulay begins with a scalar unit `1` and `n` mutually orthogonal primitive unit vectors:

```text
i1, i2, …, in
```

The key laws are:

```text
ia² = −1
ia ib = −ib ia     when a ≠ b
```

Scalars commute with all generators. The paper says that the ordinary laws of algebra apply except for commutativity of multiplication: multiplication is therefore intended to remain associative. A product of primitive generators is a **primitive vectorium**.

For example, every multenion can be decomposed into components by the number of distinct primitive vectors in a product:

```text
q = V0q + V1q + V2q + … + Vnq.
```

`Va q` denotes the component of **homogeneity** (modern readers would usually say *grade*) `a`.

| McAulay term | Meaning in the paper | Approximate modern bridge |
| --- | --- | --- |
| scalar / `V0` | grade-zero part | scalar |
| vector / `V1` | grade-one part | vector |
| `Va` / hypervector | homogeneous grade-`a` component | grade-`a` multivector |
| multenion | sum of all grades | multivector-like element |
| primitive vectorium | product of distinct primitive units | basis blade-like product |
| vectorium | `Va` applied to a product of vectors | exterior-product-like graded product |
| linity | linear function/operator | linear map |

This is recognizably close to a Clifford-algebra presentation with negative-definite generator squares. That is a modern interpretive bridge, not terminology McAulay uses as his primary framework.

### Dimension and independence (§2)

The elementary products generate `2^n` combinations. McAulay proves an independence theorem for mutually anticommuting multenions whose squares are nonzero scalars. In the even-`n` case, he states that a general multenion requires `2^n` independent scalar coefficients; for `n = 4`, that is sixteen.

He notes a qualification for odd `n`: if the product of all generators is scalar, only `2^(n−1)` combinations are independent. He then elects, for general multenion theory, to treat the full product as independent even when `n` is odd.

This matters for any implementation claim: the paper’s general `n = 4` system is a 16-component graded algebra, not an eight-component algebra.

### Even subalgebra and quaternions (§2)

The even-grade elements form a subalgebra of dimension `2^(n−1)`. McAulay relates quaternionic cases to this structure, discussing both `n = 3` and `n = 4` perspectives. His concern is not merely to rename quaternions, but to retain a richer graded setting in which quaternion-like pieces appear as substructures.

## Grade projection and the capital linities (§1–§3)

The grade projections `Va` are linear operators. McAulay states that they commute, are idempotent, and annihilate each other when their grades differ:

```text
Va² = Va
VaVb = 0  when a ≠ b.
```

He then introduces a set of useful operators, which he calls **capital linities**.

### `P`, `K`, and `Q`

- `Pa` reverses the sign of every occurrence of the generator `ia`.
- `P = P1P2…Pn` reverses the sign of every primitive vector and separates even from odd grade:

  ```text
  P(0)q = ½(1 + P)q = q0 + q2 + q4 + …
  P(1)q = ½(1 − P)q = q1 + q3 + q5 + …
  ```

- `K` reverses the order of primitive factors while also changing each primitive-vector sign according to McAulay’s convention. It is **retrospective**:

  ```text
  K(qr) = Kr Kq.
  ```

- `Q = PK = KP` is another reversal/sign operator.

McAulay distinguishes operators that preserve product order (**proscriptive**, in his terminology):

```text
φ(qr) = φq · φr
```

from retrospective operators that reverse it. He also defines conjugacy of a linity through scalar-part pairings. These operators are not decorative notation: they provide systematic ways to select grades, reverse products, define reciprocal/dual-like objects, and express invariant forms.

## The commutation theorem (§3)

If homogeneous elements `u` and `v` have grades `a` and `b`, the possible grades in their product differ by steps of two. McAulay derives formulas that separate the commutative and anticommutative combinations of `uv` and `vu` into selected grade components.

For vectors `α` and `β`, the familiar special case is:

```text
V0(αβ) = ½(αβ + βα)
V2(αβ) = ½(αβ − βα)
```

So the symmetric combination is the scalar/inner part and the antisymmetric combination is the bivector part. This is one of the clearest bridges between the paper’s notation and later geometric-algebra practice.

The general theorem is important because it tells the reader how signs and grades change when factors are reordered. That control is needed in the later invariant calculations.

## Rotations (§4)

McAulay distinguishes several senses in which the primitive vectors might be transformed. The key form is conjugation by an invertible multenion:

```text
r′ = q r q⁻¹.
```

This changes the primitive generators to `qi_aq⁻¹`. But he argues that not every such substitution has the geometric grade-preserving character wanted for a rotation.

For the intended continuous rotations, `q` is restricted to a product of vectors, leading infinitesimally to a bivector-like generator `ω` and finitely to:

```text
r′ = e^ω r e^(−ω).
```

The infinitesimal change has commutator form:

```text
du′ = ½(dω u′ − u′ dω).
```

The resulting lesson is precise: the grade-two part is the generator of infinitesimal rotation, and a rotation must be checked for its action on grades rather than inferred merely from invertibility.

## Vectoriums and normal reciprocals (§5)

For vectors `α1, …, αa`, McAulay defines a vectorium by taking the grade-`a` part of their product:

```text
Va(α1 α2 … αa).
```

He establishes its multilinearity and sign reversal under exchange of two arguments. This is the paper’s Grassmann-like combinatorial product.

Given `n` linearly independent vectors, the paper constructs `2^n` vectoriums and a corresponding set of **normal reciprocals**. Their scalar-part pairings satisfy a dual-basis relation:

```text
V0(ᾰ α̂) = 1
V0(ᾰ1 α̂) = 0  for a non-corresponding pair.
```

This yields component-extraction and reconstruction formulas for a general multenion. In plain terms, the reciprocal system lets the coefficient of a basis object be recovered by an invariant scalar pairing.

## Extended vector linities (§6)

A vector linity `φ` is extended from vectors to every grade by acting on every vector factor before forming the vectorium:

```text
Φ Va(α1 α2 … αa) = Va(φα1 · φα2 … φαa).
```

McAulay proves that extension respects composition and inversion:

```text
(φ)(ψ) = (φψ)
(φ)⁻¹ = (φ⁻¹).
```

He also relates the conjugate of the extended linity to the extension of the conjugate. This is the mechanism that carries a vector-level transformation consistently to scalars, bivectors, and the rest of the graded system.

**Implementation reading:** an operation on a grade-`a` object must be defined through its action on the underlying vectors and its grade projection; it is not licensed merely by an informal analogy with vector code.

## Higher product identities (§7)

Section 7 develops extensive identities generalizing quaternion formulas involving products of two and three vectors. It uses paired projections—written with `Λ` and `Λ′`—to track the grade families that are concordant with different possible product grades.

The role of this section is structural rather than introductory:

- it gives controlled formulas for reassociating and reordering projected products;
- it tracks the sign changes introduced by grade and order;
- it generalizes identities familiar from quaternion vector calculus;
- it supplies algebraic tools used in the later differential-invariant development.

This section is not a license to ignore parentheses. The paper assumes an associative multiplication law from the outset; its transformations of expressions are derived identities inside that associative setting.

## Differential and geometric programme (§§8–22)

From §8 onward, McAulay applies the algebra to differential invariants and geometry. The notation becomes specialized and dense, but the progression is intelligible.

| Sections | Main task |
| --- | --- |
| §8 | Integration: builds differential and integral relations in multenion notation. |
| §9 | Covariants and contravariants: distinguishes transformation behaviour under changes of variables. |
| §10 | Differentiation: organizes differential operations suggested by the integration theorems. |
| §§11–13 | Defines a fundamental covariant vector linity and develops invariant forms plus normal/incident components. |
| §14 | Applies the framework to Riemann and Weyl manifolds. |
| §15 | Defines absolute differentiation along a path or field. |
| §16 | Develops curvature. |
| §17 | Compares the multenion formulation with tensor theory. |
| §18 | Discusses Eddington’s contemporary work and adds corrections. |
| §19 | Proposes notational and terminological improvements. |
| §20 | Treats Maxwell equations for bulk matter. |
| §21 | Uses stationary action in a Riemann manifold. |
| §22 | Adds a complementary-object construction and further contraction identities. |

The recurring purpose is to replace large indexed tensor expressions with algebraic products, grade selections, and linities while preserving covariant/invariant meaning.

## `n = 4`, semi-real systems, and relativity

McAulay repeatedly treats `n = 4` as a special case because it has sixteen independent scalar components and admits particular decompositions useful for relativity-era calculations.

He introduces a **semi-real** substitution in which one generator is written with a square `+1` after a factor involving the scalar imaginary unit. This is his route to expressions such as spatial-vector terms plus a time-like term. The construction belongs to his own notation and historical goals; it should not be casually equated with modern signatures, spinors, or a current physical theory without a separate translation and verification.

## What the paper establishes, and what it does not

### Supported by the source

- McAulay defines an associative, noncommutative, graded algebra generated by `n` anticommuting units whose squares are `−1`.
- A general `n = 4` multenion has sixteen independent scalar components in the paper’s intended general theory.
- Grade projections, reversal/sign linities, vectoriums, reciprocal systems, and extended linities are explicit parts of the formal programme.
- The paper treats rotations, invariants, covariants, differentiation, curvature, and physical applications through that framework.
- Quaternion language appears as an important comparison and substructure, not as the whole of the theory.

### Not supported by the source alone

- A claim that McAulay’s multenions are an eight-component octonion algebra.
- A claim that the product is nonassociative. Law I assumes the ordinary algebraic laws other than commutativity; the paper’s product manipulations rely on associativity.
- A claim that the paper specifies a finite-state algorithm, Forth implementation, ROM image, GA144 program, or silicon circuit.
- A claim that the historical differential-geometric or physical applications are current accepted physics.
- A uniqueness claim that McAulay was the only later user or exponent of “multenions.” That needs bibliographic research beyond this single text.

## Safe project uses

The paper can responsibly support the following episode-level claims:

- McAulay proposed a richly graded, explicit algebraic language for geometry and differential invariants.
- His construction begins from named generators and stated multiplication rules, then derives higher structures through grade projection and linear operations.
- The paper makes the organisation of an algebra visible: basis, grade, transformation rule, composition, and invariant pairing all have names and formal roles.
- The transition from an algebraic object to a computation still requires a separate algorithm: representation, input, state, transition rule, error condition, and evidence of execution.

The last point is especially important for the series. McAulay supplies historical formal material, but no direct proof that a proposed modern controller is a realization of his calculus. Any claimed correspondence must identify the source object, its modern representation, the permitted operation, the preserved identity, and the test that could falsify the mapping.

## Suggested reading route

For the historical algebraic core:

1. §1: laws, grades, definitions, and capital linities.
2. §2: independence, dimension, even subalgebra, and quaternion relationship.
3. §3: commutation and scalar/bivector decomposition for vectors.
4. §4: rotations and their bivector infinitesimal generator.
5. §§5–6: vectoriums, reciprocal systems, and extension of vector linities.

For the differential-invariant programme:

6. §7 for higher product identities.
7. §§8–17 in order, with a separate notation sheet.
8. §§18–22 as historical applications, corrections, and extensions.

## Citation form

For internal project use, cite the source by section rather than loose page number:

> Alexander McAulay, “Multenions and Differential Invariants,” §[number], in the project PDF edition.

The section number gives a future script or research note a stable route back to the exact formal claim being used.
