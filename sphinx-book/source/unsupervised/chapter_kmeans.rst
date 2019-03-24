K-Means Clustering
=====================


Learning Objectives

- Understand data clustering  
  
- Learn the k-mean algorithm

- Write a test generator for creating test cases

- Implement the algorithm in Python

  
Clustering Data
---------------


Consider the following scenario: A department store is planning the
annual promotion. The store wants to give customers discount coupons
based on their purchase history.  If a customer has purchased a desk
at this store, the customer is given a coupon for a desk.  If a
customer has purchased shoes, the customer is given a coupon for
shoes.  If a customer has purchased a jacket, the customer is given a
coupon for a jacket.  The store sells thousands of products and it
does not want to give one type of coupon for each product because
doing so would create thousands of types of coupons.  It would be too
expensive making so many types of coupons and programming the checkout
machines to recognize these many types of coupons.  Instead, the store
wants to provide only a few (say 10) types of coupons.  The store
wants to group the customers based on what they bought together.  For
example

\begin{itemize}

- If a customer has bought shirts, shoes, and a sweater together,  this customer is given a coupon for clothes.

- If another customer has bought a desk, a dining table, and four chairs, this customer is given a coupon for furniture.

- If a third customer has bought a tie and shoes, this customer also receives a coupon for clothes (not for furniture).

- If the fourth customer has bought chair and a desk, this customer receives a coupon for furniture (not for clothes).


The problem is that the store does not know how to group the customers
so that the same group of customers gets the same coupon.  In other
words, the store wants to divide the customers into groups so that the
customers in each group have bought similar items.  The discussion
above assumes that customers would likely buy what they have already
bought.  In reality, stores would give customers coupons for what they
may buy later.  For example, if a customer has bought a desk, the
customer is unlikely to buy another desk soon.  Instead of giving a
coupon for another desk, the store may give a coupon for buying a
chair.  If a customer has bought a jacket, the store may give a coupon
for a sweater.


Consider another example: A research project wants to find the
commonalities among lung cancer patients. They want to divide the
patients into group based on personal information and behavior, such
as age, location, occupation, education, marital status, diet, amounts
of sleep, the food they eat, etc. They want to know whether one group
has more patients than the other groups.

.. index::
   unsupervised learning
   unsupervised learning: clustering

Both examples are *clustering* problems: these problems divide
data (people in both cases) into groups so that the data inside each
group is similar and the data in different group is dissimilar.  This
is unsupervised learning because there is no teacher telling computers
whether two pieces of data belong to the same group.  The correct
answer depends on the other pieces of data.

Clustering into Groups
----------------------

.. index::
   unsupervised learning: clustering: k-mean

Consider the department store coupon problem again. Suppose the store
decides to issue exactly ten types of coupons.  The problem becomes
dividing the customers into ten groups based on their purchase
history.  This section describes the *k-mean clustering algorithm*;
here, :math:`k` is a number assigned to the problem as the number of groups.
For the department store, :math:`k` is 10.  Before explaining how this
clustering method works, let us understand what this method wants to
accomplish.  An obvious question is how to decide the value of
:math:`k`. This book will discuss that later.

Suppose there are :math:`n` data points (each point is a person): :math:`x_1`,
:math:`x_2`, ..., :math:`x_n`. Each data point is a vector.
The department store considers these products:

- refrigerator
- washer
- dryer
- jackets
- shirts
- shoes
- pants
- sweaters

For example, :math:`x_1 = <1, 0, 0, 3, 5, 0, 0, 2>` means that in the past
twelve months the first customer has bought one refrigerator, no
washer, no dryer, three jackets, five shirts, no shoes, no pants, and
two sweaters.  If :math:`x_2 = <0, 1, 1, 0, 0, 1, 0, 0>` means the second
customer has bought no refrigerator, one washer, one dryer, no
jackets, no shirts, one pair of shoes, no pants, and no sweater.

Define K-Mean Clustering Problem
--------------------------------

We want to group these :math:`n` data points into :math:`k` clusters:
:math:`C_1`, :math:`C_2`, ..., :math:`C_k`. Obviously :math:`k` must
not exceed :math:`n`. In reality, :math:`k` is usually much smaller
than :math:`n`, i.e., :math:`k << n`.  Each cluster contains a set of
data points.  In this book, a vector uses a lower case letter such as
:math:`x`. A set uses an upper case letter such as :math:`C`. The
following properties must be satisfied:

- A data point must belong to one cluster: :math:`\forall i, 1 \le i \le
  n, \exists m, 1 \le m \le k`, such that :math:`x_i \in C_m`. This means
  for any value of :math:`i` between 1 and :math:`n` (inclusively), there is a
  value :math:`m` between 1 and :math:`k` (inclusively), such that :math:`x_i` is an
  element of :math:`C_m`.

  
- Each cluster contains one or more data points, i.e.,
  :math:`|C_j| \ge 1`, for :math:`1 \le j \le k`.  In other words, an
  empty cluster cannot be accepted.
  
- The clusters together includes all data points: :math:`C_1 \cup C_2
  \cup ... \cup C_k = \{x_1, x_2, ..., x_n\}`.

- A data point must not belong to two or more clusters: :math:`\forall
  i, 1 \le i \le n` if :math:`x_i \in C_j` and :math:`x_i \in C_m` then :math:`j = m`,
  here :math:`1 \le j, m \le k`.  To put it in another way, :math:`C_j` and :math:`C_m`
  has no overlap if :math:`j \ne m`: :math:`C_j \cap C_m = \emptyset`.

  
How is the problem defined? Suppose :math:`D` (as distance) defines
how dissimilar the data points of each cluster.  If the data points
are quite similar, :math:`D` is small.  If the data points are
quite dissimilar, :math:`D` is large.  The goal is to assign :math:`x_1`,
:math:`x_2`, ..., :math:`x_n` to :math:`C_1`, :math:`C_2`, ..., :math:`C_k` so that

:math:`\min \underset{j = 1}{\overset{k}{\sum}} D(C_j)`

is as small as possible.


This is a *minimization problem*. A minimization problem aims to make
a quantity, called the *cost function*, as small as possible.
Minimization problems are *optimization problems*, so are
*maximization problems*.  A maximization problem aims to make a
quantity, called the *profit function* or *score function*, as large
as possible.

.. index::
   cost function
   profit function
   minimization problem
   maximization problem
   optimization problem

How is :math:`D` defined?  It can be defined in many ways. One commonly
used definition is the sum of pairwise Euclidean distance:

.. index::
   Euclidean distance


:math:`D(C_j) = \underset{x_r, x_s \in C_j}{\sum} (x_r - x_s)^ 2`


If :math:`x_r` and :math:`x_s` are :math:`p`-dimensional vectors:
:math:`x_r = (x_{r1}, x_{r2}, ..., x_{rp})` and
:math:`x_s = (x_{s1}, x_{s2}, ..., x_{sp})`.
The distance of them is defined as the sum of the square
of the difference in each dimension:

:math:`(x_r - x_s)^ 2 = \underset{i = 1}{\overset{p}{\sum}} (x_{ri} - x_{si})^2`.
