"""

file: Homework3-4.py
language: python3
author: tpm6421 : Trisha P Malhotra
question:
(a) Write a function sortedHasSum that takes a sorted array S of n
numbers and another number x, and returns a Boolean indicating whether or not
there is a pair of numbers in S whose sum is x that is O(n).
Your implementation may not use a hash table (or any auxiliary data structure).
(b) Write a function hasSum that is O(n log(n)) that does the same thing when S
is an arbitrary array of numbers. Your implementation may not use a hash table
(or any auxiliary data structure).

"""

def sortedHasSum(sorted_array, x):
    """
    
    :param sorted_array: sorted list of numbers
    :param x: to be found as a sum
    :return: 
    """
    result = False
    x = int(x)
    value = int(sorted_array[0]) + int(sorted_array[-1])
    if value == x:
        return True
    elif value < x:
        for i in range (len(sorted_array)-2, 0,-1):
            value = int(sorted_array[len(sorted_array)-1]) + int(sorted_array[i])
            if value == int(x):
                return True
    else:
        for i in range(1, len(sorted_array) - 1):
            j = 0
            if int(sorted_array[0]) == 0:
               j = 1
            value = int(sorted_array[j]) + int(sorted_array[i])
            if value == int(x):
                return True
    return result



def hasSum(unsorted_array, x):
    """
    
    :param unsorted_array: unsorted list of numbers
    :param x: to be found as a sum
    :return: 
    """
    sorted_array = merge_sort(unsorted_array = [int(y) for y in unsorted_array.split(" ")])
    return sortedHasSum(sorted_array, x)


def merge_sort(unsorted_array):
    """
    
    :param unsorted_array: 
    :return: 
    """
    i = 0; j = 0; k = 0
    if 1 < len(unsorted_array):
        m = len(unsorted_array) // 2
        left = unsorted_array[:m]
        right = unsorted_array[m:]
        merge_sort(left)
        merge_sort(right)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1
        if j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1
        if i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1
    return unsorted_array

def main():
    """
    S : sorted array and then renewed as array of arbitrary values
    x : number to be checked for having a pair that adds up to this .
    :return:
    """

    S = "8 3 7 12 7 3 9 0 6 7 8 9 1 3 0"
    x = 6
    result = hasSum(S, x)
    print("x used is : " + str(x))
    print("Sum present in the given list,using hasSum: " + str(result))

    #============================

    S = "0 1 3 5 6 7 8 9"
    S = [int(y) for y in S.split(" ")]
    res = sortedHasSum(S, x)
    print("Sum present in the given list,using sortedHasSum: " + str(res))


main()