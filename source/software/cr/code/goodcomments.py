#!/usr/bin/python3
# goodcomments.py

def bubbleSort(arr):
    """Sorts an array in ascending order.
      
      :param arr: The array to be sorted.
      :type arr: int[]
    """
    n = len(arr)
    # Iterate through all elements n and its pairs
    # in positions greater than it
    for i in range(n):
        for j in range(0, n-i-1):
        # Swap elements when the left element 
        # is larger than the right element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]