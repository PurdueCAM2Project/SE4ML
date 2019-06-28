Principal Component Analysis
============================

Machine learning solutions are often designed to handle high-dimension
data. For example, the prices of houses may be affected by dozens of
factors, such as locations, sizes, years, number of floors, presence
of basements, types of materials, sizes of yards, distances to parks,
etc.  Among all these factors, it is natural to ask "Which factor has
the greatest effects on the prices?"  Principal component analysis
(PCA) is a method to answer such a question.  PCA aims to "transform"
high-dimensional data so that the "principal components" can be
expressed in lower dimensions.  To put in another way, PCA aims to
discover which components have the greatest impacts in the data.
Before we get into the details of PCA, let's first consider some examples.

Examples
--------

Consider an ellipse. There are two common ways to express an ellipse:

:math:`\frac{x^2}{a ^ 2} + \frac{y^2}{b ^ 2} = 1`

.. or \langle \lbrace { x = a \cos(t) \atop y = b \sin(t) }

   

       

(Figure: Ellipse)

review Linear
Algebra.
