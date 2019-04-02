"""
Algorithms:Homework 4, qn 1

author : Trisha P Malhotra, tpm6421
"""


def max2( num1, num2):
    """

    :param num1: first integer number
    :param num2: second integer number
    :return: maximum_result
    """
    # Getting difference between the two numbers:
    num_diff = num1 - num2
    # Now, if MSB of c is negative , it implies num1 is smaller than num2,
    # else, vice-versa
    # So, we bit-sight-shift by 31 positions , to get the signed bit at rightmost bit(LSB)
    MSB_of_num_diff = (num_diff >> 31) & 0x1

    maximum_result = num1 - MSB_of_num_diff * num_diff
    return maximum_result


def main():
    print("Running program to get Maximum among two integers...")
    x = int(input("Enter first number :"))
    y = int(input("Enter second number :"))
    print("Maximum value is :")
    print(max2(x,y))

main()