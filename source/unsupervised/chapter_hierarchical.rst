Hierarchical Clustering
========================

Learning Objectives


- Understand hierarchical clustering algorithm

- Learn the binary tree and its properties

- Use the tree's properties to gain insight of data
  
- Implement the algorithm for hierarchical clustering

    
Limitations of the k-mean Algorithm
-----------------------------------


The previous chapter explains the k-mean clustering algorithm.  It is
simple and useful as an initial analysis of data but it also
has several major problems:

- There is no obvious reason to select a particular value of `k`.  The previous chapter shows an example: the data is generated for 10 clusters but the smallest distance occurs when ``k`` is 13.

- The algorithm is non-deterministic and it is often necessary running the same program multiple times.

- For a given cluster, there is no easy answer which other cluster is  closer.  It is possible to calculate the distances of centroids but  this requires additional work.

- The k-mean algorithm assigns all data points to one of the ``k``  clusters in the very first step.  Then the algorithm adjusts the  clusters by the finding closest centroid from each data  point. Because the initial assignments have direct impacts on the  final results, the program often needs to run multiple times for  selecting better results.

*Hierarchical Clustering* is a method that does  not have these same problems as the k-mean algorithm.


Examples of Hierarchical clustering
-----------------------------------

Hierarchical clustering iteratively finds the closest pair of clusters
(at the beginning, each data point is a cluster by itself).  The
algorithm makes the pair two children of a binary tree.  For
hierarchical clustering, it is called *dendrogram*, instead of binary
tree. This book uses both terms interchangably.  The tree node becomes
a new cluster.  The algorithm continues until only one tree node is
left.  Before formally describing the algorithm, let us go through
several examples.  The simplest case is when there is only one data
point but it is not very meaningful. Thus, let us start with two data
points.

+-------+-----+-----+
| index |  x  |  y  |
+=======+=====+=====+
|   0   | -66 |  45 |
+-------+-----+-----+
|   1   |  95 | -84 |
+-------+-----+-----+

They are the two children of a binary tree:

.. figure:: hierarchical/figures/cluster2.png

	    Two data points are the two children of a binary tree.


Next, we consider the case when there are four data points:

+-------+-----+-----+
| index |  x  |  y  |
+=======+=====+=====+
|   0   | -66 |  45 |
+-------+-----+-----+
|   1   |  95 | -84 |
+-------+-----+-----+
|   2   | -35 | -70 |
+-------+-----+-----+
|   3   | 26  |  94 |
+-------+-----+-----+

We use the *Euclidean distance* here. Consider two data points:
:math:`(x_a, y_a)` and :math:`(x_b, y_b)`. The distance between them
is defined as

:math:`\sqrt{(x_a - x_b)^2 + (y_a - y_b)^2}`.

Consider three data points: :math:`(x_a, y_a)`, :math:`(x_b, y_b)`,
and :math:`(x_c, y_c)`.  The following inequality is true.
      
:math:`\sqrt{(x_a - x_b)^2 + (y_a - y_b)^2} > \sqrt{(x_a - x_c)^2 + (y_a - y_c)^2}  \Leftrightarrow ((x_a - x_b)^2 + (y_a - y_b)^2) > ((x_a - x_c)^2 + (y_a - y_c)^2)`.

We care about only the order of the distance so we do not really care
about the square root.


The following table shows :math:`(x_a - x_b)^2 + (y_a - y_b)^2`
between the pairs of the data points.


+---+-------+-------+-------+-------+
|   |  0    | 1     | 2     | 3     |
+===+=======+=======+=======+=======+
| 0 |  0    | 42562 | 14186 | 10865 | 
+---+-------+-------+-------+-------+
| 1 | 42562 | 0     | 17096 | 36445 |
+---+-------+-------+-------+-------+
| 2 | 14186 | 17096 | 0     | 30617 |
+---+-------+-------+-------+-------+
| 3 | 10865 | 36445 | 30617 | 0     |
+---+-------+-------+-------+-------+


The shortest distance (10865) occurs between :math:`(x_0, y_0)` and
:math:`(x_3,y_3)`.  They are the first pair to be put into the same
cluster.  Thus, points 0 and 3 are the two children of the same parent
node.  


.. figure:: hierarchical/figures/cluster4.png

	    Clusters of four data points. Do not worry about the colors, nor the numbers along the vertical axis. Pay attention to the shape only.

	    
How do we represent the cluster that includes points 0 and 3?  There
are several different commonly used representations.  This example
uses the centroid method: a cluster is represented by the centroid of
the data points in the cluster.  The cluster that contains
:math:`(x_0, y_0)` and :math:`(x_3, y_3)` is represented by
:math:`(\frac{-66+26}{2}, \frac{45+94}{2}) = (-20, 69.5)`.  This
cluster is marked as the new :math:`(x_0, y_0)` and :math:`(x_3, y_3)`
no longer exists.  We can recompute the distances among the pairs of
points:

TO DO: make the table align right

+---+-------+-------+-------+-------+
|   |  0    | 1     | 2     | 3     |
+===+=======+=======+=======+=======+
| 0 |  0    | 42562 | 14186 | 10865 | 
+---+-------+-------+-------+-------+
| 1 | 42562 | 0     | 17096 | 36445 |
+---+-------+-------+-------+-------+
| 2 | 14186 | 17096 | 0     | 30617 |
+---+-------+-------+-------+-------+
| 3 | 10865 | 36445 | 30617 | 0     |
+---+-------+-------+-------+-------+


The shortest distance (10865) occurs between :math:`(x_0, y_0)` and
:math:`(x_3,y_3)`.  They are the first pair to be put into the same
cluster.  Thus, points 0 and 3 are the two children of the same parent
node.  


	    
How do we represent the cluster that includes points 0 and 3?  There
are several different commonly used representations.  This example
uses the centroid method: a cluster is represented by the centroid of
the data points in the cluster.  The cluster that contains
:math:`(x_0, y_0)` and :math:`(x_3, y_3)` is represented by
:math:`(\frac{-66+26}{2}, \frac{45+94}{2}) = (-20, 69.5)`.  This
cluster is marked as the new :math:`(x_0, y_0)` and :math:`(x_3, y_3)`
no longer exists.  We can recompute the distances among the pairs of
points:

TO DO: make the table align right

+---+----------+----------+----------+
|   |  0       | 1        | 2        |
+===+==========+==========+==========+
| 0 | 0.0      | 36787.25 | 19685.25 |
+---+----------+----------+----------+
| 1 | 36787.25 | 0        | 17096    |
+---+----------+----------+----------+
| 2 | 19685.25 | 17096    | 0        |
+---+----------+----------+----------+


Now, the shortest distance (17096) occurs between :math:`(x_1, y_1)`
and :math:`(x_2, y_2)`.  These two data points are the two children of
a tree node.  At this moment, there are only two clusters and they are
the children of a binary tree node.  The final result is shown below

.. figure:: hierarchical/figures/cluster4.png

	    Clusters of four data points. Do not worry about the colors, nor the numbers along the vertical axis. Pay attention to the shape only.

Next, let's add two more data points.


+-------+-----+-----+
| index |  x  |  y  |
+=======+=====+=====+
|   0   | -66 |  45 |
+-------+-----+-----+
|   1   |  95 | -84 |
+-------+-----+-----+
|   2   | -35 | -70 |
+-------+-----+-----+
|   3   | 26  |  94 |
+-------+-----+-----+
|   4   | 15  | 20  |
+-------+-----+-----+
|   5   | 66  | -3  |
+-------+-----+-----+


The pair-wise distances is shown below


+---+-------+-------+-------+-------+-------+-------+
|   | 0     | 1     | 2     | 3     | 4     | 5     | 
+===+=======+=======+=======+=======+=======+=======+
| 0 | 0     | 42562 | 14186 | 10865 | 7186  | 19728 |
+---+-------+-------+-------+-------+-------+-------+
| 1 | 42562 | 0     | 17096 | 36445 | 17216 | 7402  |
+---+-------+-------+-------+-------+-------+-------+
| 2 | 14186 | 17096 | 0     | 30617 | 10600 | 14690 |
+---+-------+-------+-------+-------+-------+-------+
| 3 | 10865 | 36445 | 30617 | 0     | 5597  | 11009 |
+---+-------+-------+-------+-------+-------+-------+
| 4 | 7186  | 17216 | 10600 | 5597  | 0     | 3130  | 
+---+-------+-------+-------+-------+-------+-------+
| 5 | 19728 | 7402  | 14690 | 11009 | 3130  | 0     |
+---+-------+-------+-------+-------+-------+-------+


The shortest distance (3130) occurs between :math:`(x_4, y_4)` and
:math:`(x_5, y_5)`.  These two data points are the two children of a
node.  This cluster is represented by the centroid :math:`(\frac{15 +
66}{2}, \frac{20 + (-3)}{2}) = (\frac{81}{2}, \frac{17}{2}) = (40.5,
8.5)`.  The cluster is expressed as :math:`(x_4, y_4)` and
:math:`(x_5, y_5)` is removed.  Now there are four data points and one
cluster.  The distances are shown in the following table:

+---+---------+---------+---------+--------+---------+
|   | 0       | 1       | 2       | 3      | 4       | 
+===+=========+=========+=========+========+=========+
| 0 | 0       | 42562   | 14186   | 10865  | 12674.5 |
+---+---------+---------+---------+--------+---------+
| 1 | 42562   | 0       | 17096   | 36445  | 11526.5 |
+---+---------+---------+---------+--------+---------+
| 2 | 14186   | 17096   | 0       | 30617  | 11862.5 |
+---+---------+---------+---------+--------+---------+
| 3 | 10865   | 36445   | 30617   | 0      | 7520.5  |
+---+---------+---------+---------+--------+---------+
| 4 | 12674.5 | 11526.5 | 11862.5 | 7520.5 | 0       | 
+---+---------+---------+---------+--------+---------+

The smallest distance is 7520.5 and it is between :math:`(x_3, y_3)`
and the cluster created earlier. Thus, :math:`(x_3, y_3)` and the
cluster are put together by making them the two childrens of a binary
tree node.  This process continues until there is only cluster left.
The final binary tree is shown below:

.. figure:: hierarchical/figures/cluster6.png

	    Cluster of the six data points.

The examples are generated using the following program:
   
.. literalinclude:: hierarchical/code/example1.py
   :language: python

Hierarchical Clustering Algorithm
---------------------------------	      

The hierarchical clustering algorithm starts by treating each data
point as a cluster. Then it repetively finds the closest two clusters.
These two clusters are the two children of a binary tree node and form
one cluster.  As a result, two clusters become one cluster.  This
process continues until only one cluster is left.  The algorithm is
described below:
    

.. figure:: hierarchical/figures/hierarchicalalgorithm.png

	    Hierarchical Clustering Algorithm

Define Distance of Two Clusters
-------------------------------   

The earlier examples use the centroid to express each cluster.  Other
definitions of clusters' distances are also used.  There are four
commonly adopted definitions for the distance of two clusters (``An
Introduction to Statistical Learning by James, Witten, Hastie, and
Tibshirani``): *complete*, *single*, *average*, and *centroid*.  They
are described below.

Suppose :math:`A = \{a_1, a_2, ..., a_n\}` is a cluster and :math:`a_1`,
:math:`a_2`, ..., :math:`a_n` are the :math:`n` data points in this
cluster.  Suppose :math:`B = \{b_1, b_2, ..., b_m\}` is another cluster
and :math:`b_1`, :math:`b_2`, ..., :math:`b_m` are the :math:`m` data
points in this cluster.  The distance between these two clusters can
be defined as
	    


-  Complete: Compute the pairwise distances of every point in  :math:`A` and every point in :math:`B`, then select the  largest distance.  Mathematically, the distance is defined as :math:`\underset{a_i \in A, b_j \in B}{\max}{|a_i - b_j|}`.   Here, :math:`|a_i - b_j|` means the distance of the two points.

-  Single. This definition considers the smallest distance  among all pairs of points in :math:`A` and :math:`B`:  :math:`\underset{a_i \in A, b_j \in B}{\min}{|a_i - b_j|}`.

-  Average. This definition computes the average of the pairwise  distances: :math:`\frac{1}{n \times m} \underset{a_i \in A, b_j \in B}{\Sigma} {|a_i - b_j|}`.


- Centroid. Find the centroid :math:`c_A` of :math:`A` and the    centroid of :math:`c_B` of :math:`B` using in Chapter of k-mean.   The distance of the two clusters is the distance of the two    centroids: :math:`| c_A - c_B|`.

  

Implementation
--------------  

Data Structures
^^^^^^^^^^^^^^^

TO DO: Explain list and tree

Procedure
^^^^^^^^^

To implement hierarchical clustering, we will use two types of data
structures: *binary tree node* and *list node*.  Each binary tree node
represents a cluster. The original data points are stored in the
*leaf* nodes and each data point is a cluster of its own. These binary
tree nodes are stored in a list.  In a binary tree, a node is a leaf
if it has no child.  Then, the cloest two clusters are fused together
into a single cluster.  The two clusters are removed from the list and
the new cluster is added to the list.  In each step, two clusters are
removed and one cluster is added.  As a result, the number of clusters
is reduced by one in each step.  This process continues until only one
cluster is left.

TO DO: Make a figure

The program's starting point is relatively simple.  It accepts one
argument as the input file. Please notice that it is different from
the k-mean solution since hierarchical clustering does not need the
value of ``k``.

TO DO: Explain the code

.. literalinclude:: hierarchical/code/main.py
   :language: python


.. literalinclude:: hierarchical/code/cluster.py
   :language: python	   

.. literalinclude:: hierarchical/code/hctree.py
   :language: python	   

.. literalinclude:: hierarchical/code/hclist.py
   :language: python	   
	            
