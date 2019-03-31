Gradient Descent
================

Learning Objectives

- Understand partial derivative and gradient

- Understand how gradient descent may be used in optimization problems

- Apply gradient descent in machine learning    

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

The derivative calculates the ratio of change in :math:`f(x)` and the
change in :math:`x` *while keeping the value of* :math:`y` *unchanged*. 

Similarly, the partial derivative of :math:`f(x,y)` with respect to
:math:`y` at point :math:`(x_0, y_0)` is defined as

:math:`\frac{\partial f}{\partial y}| _{(x_0, y_0)} = \frac{d}{dy} f(x, y_0) | _{y = y_0} =\underset{h \rightarrow 0}{\text{lim}} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h}`
      
