#!/usr/bin/python3
# edgecase.py

def findMaxVal(arr):
    """Find the maximum value in an array.
    
    :param arr: The array to be searched. Must contain at least one element.
    :type arr: int[]
    :return: The maximum value.
    :rtype: int
    """
    # Ensure there is at least one element in the array
    if len(arr) > 0:
        # Initialize the max value to the first value of the array.
        max = arr[0]

        # Iterate through the array, skipping the first value
        for i in arr[1:]:
            # If the current value is greater than the max value
            if max < i:
                max = i # Make the current value the max value
        return max
    # Otherwise, raise an error that there is an empty array
    else:
        raise ValueError("Array must have length of at least 1.")
        