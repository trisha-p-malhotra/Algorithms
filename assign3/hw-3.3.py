"""
file: Homework-3-3.py
language: python3
author: tpm6421 : Trisha P Malhotra

question: transform the tail-recursive binary search algorithm
on arrays involving the two functions search and searchHelp
into a single imperative procedure search that performs the search
using a while-loop. It should take the same arguments and
return the same results as the tail-recursive formulation in the notes.

"""

import math


def search(input_list, value, start, end):
    """
    
    :param input_list: input list of numbers
    :param value: number to be searched 
    :param start: first position in the list
    :param end:  last position in the list
    :return: 
    """

    value = int(value)
    min = start
    max = end
    while min <= max :
        middle = min + math.floor((max - min) / 2)
        if value < int(input_list[middle]):
            max = middle -1
        elif value > int(input_list[middle]):
            min = middle + 1
        elif value == int(input_list[middle]):
            return True
    return False


def main():
    input_list = "2 3 4 5 6 8"
    input_list = [int(x) for x in input_list.split(" ")]
    length = (len(input_list)-1)
    print(search(input_list, 20, 0, length))


main()