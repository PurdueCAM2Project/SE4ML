#!/usr/bin/python3
# badcomments.py

def findMaxVal(arr):
    """Find the maximum value in an array.
    
    :param arr: The array to be searched. This should be only non-negative numbers.
    :type arr: int[]
    :return: The maximum value.
    :rtype: int
    """
    # Initialize the max value to a negative number 
    # since this is guaranteed to be smaller than
    # the smallest value in the array.
    max = -1

    # Iterate through the array
    for i in arr:
        # If the current value is greater than the max value
        if max < i:
            # print("Found max!", "Value: ", i, "Old Max: ", max)
            max = i # Make the current value the max value
    return max
    