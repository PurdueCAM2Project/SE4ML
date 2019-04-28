Gradient Descent
================

Learning Objectives

- Understand partial derivative and gradient

- Understand how gradient descent may be used in optimization problems

- Apply gradient descent in machine learning

This chapter starts with a review of multivariable calculus.    
    

Partial Derivative
------------------

In Calculus, you have learned the concept of derivative. Suppose
:math:`f(x)` is a function of a single variable :math:`x`. The
derivative of :math:`f(x)` with respect to :math:`x` is defined as

:math:`f'(x) = \frac{d}{dx} f(x) = \underset{h \rightarrow 0}{\text{lim}} \frac{f(x + h) - f(x)}{h}`

The derivative calculates the ratio of change in :math:`f(x)` and the
change in :math:`x`. A geometric interpretation is the slope of
:math:`f(x)` at a specific point of :math:`x`.

Extend that concept to a multivariable function. Suppose :math:`f(x,
y)` is a function of two variables :math:`x` and :math:`y`. The
partial derivative of :math:`f(x,y)` with respect to :math:`x` at
point :math:`(x_0, y_0)` is defined as

:math:`\frac{\partial f}{\partial x}| _{(x_0, y_0)} = \frac{d}{dx} f(x, y_0) | _{x = x_0} =\underset{h \rightarrow 0}{\text{lim}} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}`

The derivative calculates the ratio of change in :math:`f(x, y)` and the
change in :math:`x` *while keeping the value of* :math:`y` *unchanged*. 

Similarly, the partial derivative of :math:`f(x,y)` with respect to
:math:`y` at point :math:`(x_0, y_0)` is defined as

:math:`\frac{\partial f}{\partial y}| _{(x_0, y_0)} = \frac{d}{dy} f(x_0, y) | _{y = y_0} =\underset{h \rightarrow 0}{\text{lim}} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h}`
      
This can be further extended to a function of :math:`n` variables :math:`f(x_1, x_2, ..., x_n)`. 
      
Gradient
--------

The *gradient* of a two-variable function :math:`f(x, y)` is at point :math:`(x_0, y_0)` is defined as

:math:`\nabla f|_{(x_0, y_0)} = \frac{\partial f}{\partial x} {\bf i} + \frac{\partial f}{\partial y} {\bf j}`

Here, :math:`{\bf i}` and :math:`{\bf j}` are the unit vector in the :math:`x` and :math:`y` directions.

Suppose :math:`{\bf v} = \alpha {\bf i} + \beta {\bf j}` is a unit
vector. Then, the amount of :math:`f`'s changes in the direction of
:math:`{\bf v}` is the inner product of :math:`\nabla f` and
:math:`{\bf v}`.  Apparently, the greatest change occurs at the
direction when :math:`{\bf v}` is the unit vector of :math:`\nabla f`.

Gradient Descent
----------------

*Gradient Descent* is a method for solving *minimization* problems.
The gradient of a function at a point is the rate of changes at that
point.  Let's consider a simple example: use gradient descent to find
a line that has the smallest sum of square error.

Linear Approximation with Least Square Error
--------------------------------------------

Consider a list of :math:`n` points: :math:`(x_1, y_1)`, :math:`(x_2,
y_2)`, ..., :math:`(x_n, y_n)`. The goal is to find the values of
:math:`a` and :math:`b` for a line :math:`\tilde{y} = a \times x + b`
such that

:math:`e(a, b)= \underset{i=1}{\overset{n}{\sum}} (y_i - (a  x_i + b))^2`

is as small as possible. This is the cumulative error. Let's call it
:math:`e(a, b)` because it has two variables :math:`a` and :math:`b`.
Here we will solve this problem in two ways: analytically and
numerically.

Analytics Method for Least Square Error
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To minimize the error function, we take the partial derivatives of
:math:`a` and :math:`b` respectively:

:math:`\frac{\partial e}{\partial a}  = 2 (a  x_1 + b - y_1)  x_1 + 2 (a  x_2 + b - y_2)  x_2 + ... + 2 (a  x_n + b - y_n)  x_n`

:math:`\frac{\partial e}{\partial a}  = 2 a (x_1^2 + x_2^2 + ... + x_n^2) + 2 b (x_1 + x_2 + ... + x_n) - 2 (x_1 y_1 + x_2 y_2 + ... + x_n y_n)`

:math:`\frac{\partial e}{\partial a}  = 2 (a \underset{i=1}{\overset{n}{\sum}} x_i^2 + b \underset{i=1}{\overset{n}{\sum}} x_i - \underset{i=1}{\overset{n}{\sum}} x_i y_i)`

For :math:`b`:   

:math:`\frac{\partial e}{\partial b} = 2 (a  x_1 + b - y_1) + 2 (a  x_2 + b - y_2) + ... + 2 (a \times x_n + b - y_n)`

:math:`\frac{\partial e}{\partial b} = 2 a (x_1 + x_2 + ... + x_n) + 2 n b  - 2 (y_1 + y_2 + ... + y_n)`

:math:`\frac{\partial e}{\partial b} = 2 (a \underset{i=1}{\overset{n}{\sum}} x_i + b n - \underset{i=1}{\overset{n}{\sum}} y_i)`          

      
To find the minimum, set both to zero and obtain two linear equations of :math:`a` and :math:`b`.
      
:math:`a \underset{i=1}{\overset{n}{\sum}} x_i^2 + b \underset{i=1}{\overset{n}{\sum}} x_i = \underset{i=1}{\overset{n}{\sum}} x_i y_i`       

:math:`a \underset{i=1}{\overset{n}{\sum}} x_i + b n = \underset{i=1}{\overset{n}{\sum}} y_i`       

The values of :math:`a` and :math:`b` can be expressed by

:math:`a =\frac{n \underset{i=1}{\overset{n}{\sum}} x_i y_i - \underset{i=1}{\overset{n}{\sum}} x_i \underset{i=1}{\overset{n}{\sum}} y_i}{n \underset{i=1}{\overset{n}{\sum}} x_i^2 - \underset{i=1}{\overset{n}{\sum}} x_i \underset{i=1}{\overset{n}{\sum}} x_i}`

:math:`b =\frac{\underset{i=1}{\overset{n}{\sum}} y_i \underset{i=1}{\overset{n}{\sum}} x_i^2 - \underset{i=1}{\overset{n}{\sum}} x_i y_i \underset{i=1}{\overset{n}{\sum}} x_i}{n \underset{i=1}{\overset{n}{\sum}} x_i^2 - \underset{i=1}{\overset{n}{\sum}} x_i \underset{i=1}{\overset{n}{\sum}} x_i}`      

TODO: examples

Gradient Descent
----------------

The gradient of a function is the direction of changes. 

:math:`\nabla e = \frac{\partial }{\partial a} {\bf i} + \frac{\partial e}{\partial b} {\bf j}`

Suppose :math:`\Delta w = \alpha {\bf i} + \beta {\bf j}` is a vector.   
	    
By definition, if :math:`\Delta w` is small enough, then the change in
:math:`\nabla e` alogn the direction of :math:`\Delta w` can be
calculated as

:math:`\Delta e = \nabla e \cdot \Delta w`.

The goal is to reduce the error. Thus, :math:`\Delta w` should be chosen to ensure that :math:`\Delta e` is negative.
If we make

:math:`\Delta w = - \eta \nabla e`,

then

:math:`\Delta e = \nabla e \cdot (- \eta \nabla e) = - \eta (\nabla e)^2`.

This ensures that the error :math:`e` becomes smaller.  The value
:math:`\eta` is called the *learning rate*.  Its value is usually
between 0.1 and 0.5.  If :math:`\eta` is too small, :math:`\Delta e`
changes very slowly, i.e., learning is slow.  If :math:`\eta` is too
large, :math:`\Delta e = \nabla e \cdot \Delta w` is not necessarily
true.

Numerical Method for Least Square Error
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to find an analytical solution for :math:`a` and
:math:`b` because the function :math:`e` is pretty simple.  For many
machine learning problems, the functions are highly complex and in
many cases the functions are not even known in advance. For these
problems, reducing the errors can be done numerically using data.
This section is further divided into two different scenarios.

- The first assumes that we know the function :math:`e` but we do not have formulaes for :math:`a` or :math:`b`.

- The second assumes that we do not know the function :math:`e` and certainly do not know the formulaes for :math:`a` or :math:`b`.

For the first case, 

:math:`\nabla e = \frac{\partial }{\partial a} {\bf i} + \frac{\partial e}{\partial b} {\bf j}`

            
:math:`\frac{\partial e}{\partial a} = 2 (a \underset{i=1}{\overset{n}{\sum}} x_i^2 + b \underset{i=1}{\overset{n}{\sum}} x_i - \underset{i=1}{\overset{n}{\sum}} x_i y_i`

      
:math:`\frac{\partial e}{\partial b} = a \underset{i=1}{\overset{n}{\sum}} x_i + b n - \underset{i=1}{\overset{n}{\sum}} y_i`

