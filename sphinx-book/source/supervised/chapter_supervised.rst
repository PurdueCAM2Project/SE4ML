Supervised Machine Learning
============================

Learning Objectives

- Understand supervised learning and the distinction from unsupervised learning
  
- Understand how supervised learning may be used
  
- Distinguish classification and regression problems

Distinguish Supervised and Unsupervised Learning
------------------------------------------------


Another type of learning is called *supervised learning*.
Unsupervised learning means discovering patterns from data, just data.
Supervised learning means associating data with *labels*. When a
father holds a baby saying "Daddy", this is supervised learning: The
baby learns to associate the father's face (data) with the sound of
"Daddy" (label). When a user identifies an email as spam and clicks
the "spam" button in a mail reader, this is supervised learning: The
mail reader learns to associate the email: the data, may include the
subject or the content or the sender, or all of them with the spam
label.

Supervised learning can be further divided into two types of problems:
*classification* and *regression*.  For classification problems, the
labels are discrete values. They can be words, numbers, a finite set
of options, etc.  The labels are discrete because it makes no sense to
have a label "between" two labels.  For example, the input is the
voice of a person and the output is the gender, either female or male.
It makes no sense to say :math:`\frac{\text{female} +\text{male}}{2}`.
That's why the labels are discrete.

Minimization Problem
--------------------

Supervised learning is essentially a "minimization problem".  Suppose
there is a collection of :math:`n` images and each image can be
represented by a word. Consider the following examples from the ``COCO
dataset``.

.. figure:: supervised/figures/coco000000006040.jpg

   Tram

.. figure:: supervised/figures/coco000000007108.jpg

   Elephant

.. figure:: supervised/figures/coco000000042070.jpg

   Bus

.. figure:: supervised/figures/coco000000124975.jpg

	    Zebra

The :math:`n` images are the sequence of inputs :math:`{\bf x} = <x_1, x_2,
..., x_n>`.  Each element :math:`x_i` :math:`(1 \le i \le n)` can be
a high-dimensional vector, such as an image. If an image has :math:`w
\times h` pixels, then :math:`x_i` is a vector of :math:`w \times h`
dimensions, each pixel represents one dimension.  For :math:`x_i`, there is
a correct word :math:`y_i` for describing the image.
:math:`{\bf y} = <y_1, y_2, ..., y_n>` is the sequence of outputs.
Please notice that :math:`{\bf x}` and :math:`{\bf y}` are sequences because
:math:`y_i` is the correct output for :math:`x_i`.  If :math:`{\bf x}` and :math:`{\bf y}`
were sets (the order in a set does not matter), then we would have problems.
      

Consider a machine model :math:`f` that intends to learn the relationships between
the inputs and outputs.
