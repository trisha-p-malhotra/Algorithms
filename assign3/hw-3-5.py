"""
file: Homework-3-5.py
language: python3
author: tpm6421 : Trisha P Malhotra

question:  Implement quicksort so that the size of the stack is O(log n)
regardless of running time. Hint: Consider the order
in which sub-problems are executed in the presence of tail-recursion.
Your implementation may not modify the partition algorithm.
"""

import math

def quick_sort_input (input_array):
    """
    :param input_array: input list of numbers

    """
    if len(input_array) < 1:
        return input_array
    else:
        return quick_Sort(input_array, 0, len(input_array)-1)

def partition(input_array, left_mark, right_mark):
    """

    :param input_array: input list of numbers
    :param left_mark: start
    :param right_mark: end
    :return:
    """

    pivot = input_array[left_mark]

    left = left_mark + 1
    right = right_mark

    flag = False
    while not flag:

        while left <= right and input_array[left] <= pivot:
            left = left + 1

        while input_array[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            flag = True
        else:
            temp = input_array[left]
            input_array[left] = input_array[right]
            input_array[right] = temp

    temp = input_array[left_mark]
    input_array[left_mark] = input_array[right]
    input_array[right] = temp

    return right


def quick_Sort(input_array, left_mark, right_mark):
    """

    :param input_array: input list of numbers
    :param left_mark: start
    :param right_mark: end
    :return:
    """
    if left_mark < right_mark:
        partition_Value = partition(input_array, left_mark, right_mark)
        quick_Sort(input_array, left_mark, partitionValue - 1)
        quick_Sort(input_array, partitionValue + 1, right_mark)
    return input_array



def main():


    input_array = "33 25 22 44 16 56 70 26 3 4 5 8"
    input_array = [int(x) for x in input_array.split(" ")]
    length = (len(input_array) - 1)
    print(quick_Sort(input_array, 0, length))


if __name__ == '__main__':
    main()