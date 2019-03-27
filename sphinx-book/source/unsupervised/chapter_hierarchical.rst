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



    
  
