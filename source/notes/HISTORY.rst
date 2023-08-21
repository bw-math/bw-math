.. _knowledge:

============================
A Brief History of Knowledge
============================

    I know that I know nothing

    -- Socrates 

How do we know things? To put a finer point on it, how do we know *that* we know things? What exactly does *knowing a thing* entail, anyway? The goal of this course is to provide, if not an exact answer, then at least a *probable* answer to this question. Make no mistake, the question is not easily answered, even in a *probable* way. In trying to uncover the answer, you will be required to think about concepts you have likely never encountered prior to this class. 

Before we begin to untangle the answer, let us take a step back and see what put us in this pickle in the first place.

Knowing Knowledge
=================

Plato 
-----

One of the first attempts (of which we are aware) to give a (*proto*-)scientific account of knowledge was produced by Plato in the 4 :sup:`th` century BCE. In his work *Thaetetus*, he tackles the subject of how we know things. The work is written as a dialogue between the titular character, a young mathematician named Thaetetus, and Plato's teacher, *Socrates*.

Toggle the excerpt of *Thaetetus* below and read through it,

.. collapse:: Thaetetus, Plato

    **Socrates**: Have you heard what they say nowadays that knowing is?

    **Theatetus**: Perhaps; however, I do not remember just at this moment.

    **Socrates**: They say it is having knowledge.

    **Theatetus**: True.

    **Socrates**: Let us make a slight change and say possessing knowledge.

    **Theatetus**: Why, how will you claim that the one differs from the other?

    **Socrates**: Well, then, having does not seem to me the same as possessing. For instance, if a man bought a cloak and had it under his control, but did not wear it, we should certainly not say that he had it, but that possessed it.

    **Theatetus**: And rightly.

    **Socrates**: Now see whether it is possible in the same way for one who possesses knowledge not to have it, as, for instance, if a man should catch wild birds--pigeons or the like--and should arrange an aviary at home and keep them in it, we might in a way assert that he always has them because he possesses them, might we not?

    **Theatetus**: Yes.

    **Socrates**: And yet in another way that he has none of them, but that he has acquired power over them, since he has brought them under his control in his own enclosure, to take them and hold them whenever he likes, by catching whichever bird he pleases, and to let them go again; and he can do this as often as he pleases.

The contents of Plato's *Theatetus* have greatly influenced the development of scientific thought in the subsequent centuries, so it is worth understanding why Plato thought what Socrates was saying was so important it should be written down for future generations. 

Socrates is making the point in the preceding lines that knowledge is not exactly the same as something you *have*, but has more in common with something you *possess*. And like a bird in a cage to which Socrates draws an analogy, you only *possess* it insofar that you *assume* control over it. The bird, however, does not *belong* to its possessor; if you were to open its cage, it would fly away and you would be none the wiser. 

Aristotle
---------

Like Socrates influenced Plato, Plato influenced Aristotle, and it would be Aristotle who would make the biggest mark on the history of thought. Of the three major Greek philosopher, Socrates, Plato and Aristotle, Aristotle was by far the most prolific. He wrote volumes of book on subjects as diverse as logic, biology, physics and art. His works were used as textbooks for centuries afterwards; more than that, entire school curriculums were oriented around learning what Aristotle saw as the three tiers (or `trivium <https://en.wikipedia.org/wiki/Trivium>`_) of primary education: grammar, logic and rhetoric. Many of his volumes are still studied to this day in universities across the world.

After learning from Plato, Aristotle moved to (LINK) and opened a famous academy named (LINK). It was there he wrote and distributed his extensive body of work. We will take a look at some of his contributions in the field of *Logic*, specifically those relating to the *character of knowledge*,

Syllogism and Induction
***********************

Aristotle viewed knowledge as a two-fold process. You start with *prior* assumptions, and then from those *prior* assumptions, you deduce conclusions. 

.. collapse:: Prior Analytics, Aristotle

    A deduction is a speech in which, certain things having been supposed, something different from those supposed results of necessity because of their being so.

The *things supposed* are now more commonly known as the "hypothesis" or the "premise", and the *results of necessity* are now more commonly known as the "conclusion" or the "consequence". A more modern phrasing of the same idea might therefore read,

    A deduction consists in assuming a hypothesis implies a conclusion and then inferring the truth of the conclusion from the truth of the hypothesis.

In anticipation of what is to come, we might be so bold as to *symbolize* this definition,

.. math::
    
    ((p \implies q ) \text{ and } p ) \implies q

Which is to be read as, "if p implies q is true and if p is true, then q is true".

Aristotle argued that all deductions like this were a form of `syllogism <https://en.wikipedia.org/wiki/Syllogism>`_, or *syllogistic reasoning*. 

Toggle the excerpt below to read through a passage of Aristotle's *Prior Analytics* where he defines a logical syllogism.

.. collapse:: Prior Analytics, Aristotle 

    In particular syllogisms, if the universal premiss is necessary, then the conclusion will be necessary...First let the universal be necessary, and let A belong to all B necessarily, but let B simply belong to some C: it is necessary then that A belongs to some C necessarily; for C falls uner B, and A was assumed to belong necessarily to all B.

Aristotle is making an important point here that can still be found in statistics today. Let us try to understand what he is saying by elaborating.

Aristotle believed you start with *universal statements*, propositions that apply to all *things* (*instances*). Then, you look at *particular cases*, and from the *universal*, you are able to draw conclusion. An example will make this clearer.

Suppose you were given the following propositions,

    *p* = All animals that are whales are also mammals.

    *q* = This animal is a whale.

    *r* = This animal is a mammal.

The first proposition, *p*, is a statement about *all* animals that are whales, or more simply, *all whales*. It asserts every instance of a *whale-thing* belongs to the :ref:`set <sets>` of mammals. This is an example of Aristotle's *universal statement*, a proposition that asserts a property belongs everything. 

The second proposition, *q*, is a statement about a *particular* animal that happens to be a whale. It asserts this case in front of us is a *whale-thing*. This is an example of an *existential statement*, a proposition that asserts a thing exists that has a certain property.

The third proposition, *r*, is the *particular* conclusion we draw by applying the *universal statement* *p* to the *particular* hypothesis *q*. If we take *p* and *q* together as true statements, then the truth of *r* must necessarily follow. 
In other words, *knowledge* is the process of inferring.

We can visualize this argument with a :ref:`Venn diagram`,

(INSERT)

In later sections, we will define the relation shown here more precisely as one of *containment* between two sets, i.e. the relation of one set **A** being wholly contained in another set **B**.

As we proceed in this class, instead of taking about *universals* and *particulars*, we will talk about :ref:`populations` and `samples`, but the same principles described by Aristotle more than two thousand years ago still hold (with slight modifications). In effect, our knowledge of *all things* allows us to draw conclusions about *particular things*.  

There is an `aporia <https://en.wikipedia.org/wiki/Aporia>`_ in this, though. In life, we are only ever presented with *particular cases*. We don't actually know that *all cats are afraid of dogs*; we only know the cats we have seen up to this point appear to be afraid of dogs. Nevertheless, from this limited sample of data, we are able to draw the conclusion *all cats are afraid of data* by inferring from *particular* cases of cats being afraid of dogs (we may even allow for the possibility of ignoring a few :ref:`outlying <outliers>` cases of particularly `bold cats <https://www.youtube.com/watch?v=8E1uBxkQxCY>`_).

TODO induction

With induction, we see the beginnings of statistical reasoning. A sample of data is observed. From this data, the common property that belongs to all its elements is abstracted. 

We close this section with a passage from another work of Aristotle. Toggle the block below to read through an excerpt of *Posterior Analytics*,

.. collapse:: Posterior Analytics

    All instruction given or received by way of argument proceeds from pre-existent knowledge. This becomes evident upon a survey of all the species of such instruction. The mathematical sciences and all other speculative disciplines are acquired in this way, and so are the two forms of dialectical reasoning, syllogistic and inductive; for each of these latter make use of old knowledge to impart new, the syllogism assuming an audience that accepts its premisses, induction exhibiting the universal as implicit in the clearly known particular. Again, the persuasion exerted by rhetorical arguments is in principle the same, since the use either example, a kind of induction or a form of syllogism.

    The pre-existent knowledge required is of two kinds. In some cases admission of the fact must be assumed, in others comprehension of the meaning of the term used, and sometimes both assumptions are essential. Thus, we assume that every predicate can be either truly affirmed or truly denied of any subject, and that 'triangle' means so and so; as regards 'unit' we have to make the double assumption of the meaning of the word and the existence of the thing. THe reason is that these several objects are not equally obvious to us. Recognition of truth may in some cases contain as factors both previous knowledge and also knowledge acquired simultaneously with that recognition-knowledge, this latter, of the particulars actually falling under the universal and therein already virutally known. For example, the student knew beforehand that the angles of every triangle are equal to two right angles; but it was only at the actual moment at which he was being led on to recognize that as true in the instance before him that he came to know 'this figure inscribed in the semicircle' to be a triangle.

Rene Descartes
--------------

For many centuries, scholars studied Aristotle, taking his word to be the final say on the matter of knowledge. Many assumed *philosophy was completed*, the work of Aristotle serving as both the climax and resolution of its whole story. There were slight fallacies discovered in his work from time to time (For example, see :ref:`Aristotle's Square of Opposition <square_of_opposition>`), but by and large, not much changed for nearly two thousand years. 

Then along came a French philosopher named Rene Descartes. You have probably encountered Mr. Descartes before, since the **Cartesian** plane is named after him. The idea of representing algebraic equations in a two-dimensional grid allegedly occured to Descartes when he was bedridden with the flu and watched a fly crawl across the ceiling of his room for hours on end. 

Descartes had many other accomplishments (such as proposing the mechanism by which the heart pumps blood through the body), but the ones we are interested in have to do with some called *skepticism*.

Cartesian Skepticism
********************

TODO 

Immanuel Kant
-------------

TODO biography

A Priori
--------

TODO 

A Posteriori
------------

TODO