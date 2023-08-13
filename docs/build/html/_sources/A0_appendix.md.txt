# Appendix I: Propositional Calculus

In what follows, you will find the definitions and explanations for the author's [Markdown]() compliant variation of propositional calculus, sometimes referred to as propostional logic or symbolic logic. This variant was adopted for ease of use with webpages. Solutions exist for JavaScript based _LaTeX_ through libraries like [MathJAX](), and perhaps if the content of this work is ever completed to the author's satisfaction, he will refactor the syntax to be more in line with general conventions, but for now, this will suffice.

## Definitions 

### Symbols

- `P()` represents a predicate function
- `#` represents the quantifier for existence
- `@` represents the quantifier for universality
- `!` represents negation
- `:` represents denotion
- `|` represents the relativizer.
- `~` represents set membership.
- `%` represents set exclusion.
- `->` represents implication.
- `&` represents conjunction.
- `v` represents disjunction.
- `<->` represents equivalence
- `=` represents equality
- `n(S)` represents the cardinality of a set _S_
- `[]` represent content separation, i.e. the "_comma_".

### Variables

- uppercase letters, such as _A_ and _B_, represents sets. 
    - `{}` also denotes a set.
- lowercase letters, such as _a_ and _b_, represents indeterminate variables.

## Propositions

A p_ropositional_, or _predicate_, function _P(-)_ is the indeterminate form of a sentence once all of its content has been abstracted away. An interesting aspect of language is encountered during this abstraction process. As the semantical concepts are subtracted step by step, distinct forms with unique, syntactical functions emerge. For instance, the prositional sentences,

- All men are mortal
- The universe is expanding

represent assertions about the state of the world. Whether or not their content is true is besides the point. Any proposition that claims to represent reality must necessarily organize itself so as to allow itself to be determined true or false; it is the structure of this organization into judgeable content prior to the judgement that is uncovered as content is abstracted. The different forms of speech have substituted in their place syntactical placeholders, so that all that remains is the form of language itself. 

To begin formalization of language, indeterminate variables, such as _x_, are assigned to the subjects of the propositions,  

- All x are mortal
- The x is expanding

In logic, once the subject matter of the sentence is made indeterminate, they can no longer be spoken of as sentences, so we coin the term, following **Tarski**, of _sentential functions_[^Tarski#1]. A sentence is _determinate_ in its meaning, whereas a sentential function is _indeterminate_ in its meaning. A sentence speaks _about_ something, whereas a sentential function shows _how_ it is spoken, once the _thing_ it is _about_ is given.

Another layer of abstraction is added by noting the subject is quantified over a certain range. _All_ in the first proposition encompasses all possibile values of _x_ as subject to assertion, where as _the_ in the second proposition separates out  a single instance of _x_ for the operation of assertion. In the jargon of logic, the first proposition is a case of _universal_ quantification, whereas the second is a case of _existential_ quantification. We reserve special, _constant_ symbols for these grammatical objects, `@` and `#` respectivey,

- @x are mortal
- #x is expanding

One of the key insights of propositional logic is the predicates of these sentences are essentially functions that operate on the indeterminate variables that form their subjects, independent of the quantification attached to the subject. The particularizing article attached to the subject, its quantification, indicates in what way the predicate is said to apply to its subject matter. We therefore introduce the predicate function `P(-)` at this point to abstract away the relations of the predicate. In order to generalize across all possible quantified propositions, we introduce relativers to synchronize the syntactical forms and make apparent their commonality,

- @x such that P(x)
- #x such that P(x)

The vagaries of English are then abstracted away in their entirety to leave out the possiblity of linguistic ambiguity, so that we are left with purely symbolic, purely formal propositions, with the introduction of the symbolic _relativizer_ `|`,

- `@x | P(x)`
- `#x | P(x)`

The object of propositional logic is understanding the syntatical conditions that must be met by any semantical staetment within a language. Propositional logic has no opinion on the content of its syntax. It can only show, once meaning is given to it, how it must operate in its formal aspect.

### Logical Basis

TODO

The _predicate_ function is to be understood as an operation that is applied to the quantified variables in a proposition.

TODO

The primitive operations that can be used to compose predicate functions are _AND_, _OR_ and _NOT_: `&`, `v` and `!`.

TODO

Negation is the only primitive operation to operate exclusively on a single predicate. In the case of one proposition, it is either `T` or `F`, so there is only one possible operation that can be applied, that of transformation into the opposite. An operation that took `T` to `T` or `F` to `F` would be of no value, for it would add nothing to the semantics we are developing. When only one predicate is considered, negation is the only possible operation that will induce a change in appearance. 

TODO

The other operations in our logical basis operate on two or more predicates. When composing two predicates, _P_ and _Q_, each has the possibility of being true or false. Therefore, there are a total of four possible states when both propositions are simultaneously considered, forming a sample of sequences,

`TT, TF, FT, FF`

Logical operations can be defined as "_occuring_" when certain outcomes in the simultanoues occurance of _P_ and _Q_ obtain. _AND_, for instance, can be defined in as what happens when both _P_ and _Q_are true. In other words, _AND_ paritions the logical space in the sequence `TT` from the sequences `TF, FT, FF`. Similarly, _OR_ can be 

These are the meta-semantical priors that must be presupposed in order to engage in logic; Their validity must be accepted prior to the semantics of propositional logic. In this respect, logic is analogue in sentential-space to the **Cartesian** coordinate system that underlies representations of geometric space; it cannot be said what exactly a coordinate axis _is_ because it is the axes which provide the basis for specifying what _is_. Likewise, _AND_, _OR_ and _NOT_ only have meaning in reference to the meaing they give to the sentiential form. 

These operations define a basis for structuring statements. What is meant by these operations cannot be further reduced to finer grained syntax; these operations cannot be justified except by direct appeal to the intellect. _They are what they are_.

TODO

It should be noted there is nothing special about _AND_ or _OR_. We could define a _NEVER_ operation to obtain when `FF` occured and a _XOR_ operation to obtain when `FT` or `TF`, and use these operations instead as basis for compounding predicate functions. 

The value in the logical operations we use to compose proposition is to be found in their ability to reach every possible state. In the case of two propositions, each possibility can be reached by some logical formulation.

- `TT` maps to `P & Q` and `P v Q`
- `TF` maps to `P v Q`
- `FT` maps to `P v Q`
- `FF` maps `![P & Q]` and `![P v Q]`

With the alternate basis of _NEVER_, _XOR_ and _NOT_, we would traverse the logical space as follows, using `x` for _XOR_ and `n` for _NEVER_,

- `TT` maps to `![P n Q]` and `![P x Q]`
- `TF` maps to `P x Q`
- `FT` maps to `P x Q`
- `FF` maps to `P n Q` and `![P x Q]`

Either way yields a logical calculus for compounding predicates. The choice of _AND_ and _OR_ over _NEVER_ and _XOR_ is a matter of convention. 

TODO

In the case of three proposition, _P_, _Q_ and _R_, the permutations of possible truth values multiply. However, the nature of logic is synthesize complexity from simpler terms. We thus want to develop laws that allow us to undertand more complex cases using by considering their constituent predicates in a pairwise fashion.

TODO

### Implication

TODO

The logical implication is often misunderstood by laymen. Implication is a syntactical form, it has no meaning in and of itself.  (Is this true?)

TODO


The syntactical form of implication can be understood in terms of the primitive logical operations introduced in the previous section. 

TODO

All other logical operations can be defined in terms of these operations. For instance `A v ~B` is logically equivalent to `B -> A`. In plain English, _A or not B is equivalent to if B, then A_. This fact can be seen by inspecting the truth tables for either compound proposition.

TODO

### Excluded Middle

The law of the excluded middle simply states that it must either be the case that _P_ or its negation is true,

`P v !P`

For example, it cannot be the case that both propositions, _12 is even_ and _12 is odd_, are simultaneously true, because the concepts of even and odd are negations of one another with respect to the natural numbers (i.e., `odd <-> !even`). The set theoretic definitions of even and odd partition the natural numbers into non-overlapping sets, therefore a number must be contained in one or the other, but not both. This is what is captured in the law of the excluded middle.

### Quantification 

The following list shows how the English language can be mapped to the semantics of propositional calculus. Examples are given letting _x_ represent an indefinite but distinct bunny rabbit, the propositional function `P(-)` represent the predicate _is fluffy_, and _A_ represents the set of bunnies which have the property of being fluffy,

---

General Quantified Propositions

---

- (Q1) **Universal Quantification**: `@x | P(x)`
    - _General_: all _x_ such that x is _P_
    - _Particular_: all bunnies are fluffy
- (Q2) **Negation of Universal Quantification**: `![ @x | P(x) ]`
    - _General_:  not all _x_ such that x is _P_
    - _Particular_: not all bunnies are fluffy
- (Q3) **Existential Quantification**: `#x | P(x)`
    - _General_: atleast one _x_ exists such that x is _P_ 
    - _Particular_: some bunnies are fluffy
- (Q4) **Negation of Existential Quantification**: `![ #x | P(x) ]`
    - _General_: no _x_ exist such that x is _P_
    - _Particular_: no bunnies are fluffy

---

Quantified Semantics

---

- (Q5) **Universally Quantified Membership** `@x | x ~ A`
    - _General_: all _x_ such that x belongs to _A_
    - _Particular_: all bunnies are _fluffy bunnies_
- (Q6) **Universally Quantified Exclusion**: `@x | x % A`
    - _General_: all x such that x does not belong to  _A_
    - _Particular_: all bunnies are not _fluffy bunnies_
- (Q5) **Existentially Quantified Membership** `#x | x ~ A`
    - _General_: all _x_ such that x belongs to _A_
    - _Particular_: all bunnies are _fluffy bunnies_
- (Q6) **Universal Exclusion**: `@x | x % A`
    - _General_: all x such that x does not belong to  _A_
    - _Particular_: all bunnies are not _fluffy bunnies_

## Sets


In the preceding, we have written `#x | P(x)` as a way of abstracting from the general proposition contained in the English sentence _there is an x that is P_ its purely formal characteristics. 

This formulation implies when a proposition is asserted, it is equivalent to applying a function to a subject, embodied in the term `P(x)`. When a subject is predicated by a descriptive clause, the predicate is transferred to the subject in its entirety, without meditation. This implies the subject _is_ the predicate. Rather, when we write `P(x)`, what we really mean is the subject _x_ has the property of having the predicate _P_. It is in their belonging to a set that objects are predicated by a property _P_. In mathematics, the thing which has a property has that property by virtue of its inclusion in a set. Sets are analogous to concepts; they are collections of objects that share the same property, and it is because they belong to this collection that predication is possible. In other words, when we write `#x | P(x)`, we are implicitly writing,

(D1) `#x | x ~ A & P(x)`

where _A_ is the set of things having the property _P_.

A set can be understood intuitively as a collection of objects. More formally, using the above definitions, a set _A_ can be defined through the symbolic proposition,

(D2) `#A | [ @x | x ~ A v A = 0 ]`

This translate roughly into the sentence: _there exists a set A such that for all x, x belongs to A or A is empty_.

### Axiom of Abstraction and Axiom of Separation

In the first attempt to formalize the foundations of mathematics, before the concept of _sets_ was well defined in its lexicon, **Frege** proposed the following _axiom of abstraction_,

(A1.1) `#A | [ @x | x ~ A <-> P(x) ]`

This translate into _there exists an A such that for all x, if and only if x belongs to A, then x has the property of belong to that set.

**Zermelo** modified the _axiom of separation_ so as to remove the possibility of **Russell**'s paradox from the possibilities of its application in the following way,


(A1.2) `#A | [ @x | x ~ A <-> x ~ B & P(x)]`

Roughly speaking, this axioms says, _given a set B, there exists a set A such that for all x, if and only if x is a member of A, then x is a member of B and has the property of belonging to the set A_.

The existence of set _B_ must be given prior to the application of the axiom, or else 
TODO

### Axiom of Extensionability

TODO

### Theorems

1. Individuation: 

## Footnotes

[^Tarski#1]: [Introduction to Logic, Chapter 1, Section TODO, YYYY,S Alfred Tarski](TODO),