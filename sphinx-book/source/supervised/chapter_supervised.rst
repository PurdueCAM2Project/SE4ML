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
