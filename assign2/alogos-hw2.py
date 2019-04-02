"""

Description: Algorithms - Homework 2 - Qn 3.
@author : Trisha P Malhotra (tpm6421@rit.edu)

Ans: Time Complexity of fibPow is O(log(n))

"""



def fibPow(M,expo):
    """
    To get the algorithm to be of the complexity O (log(n)),
    we call this function recursively to multiply the matrix to power expo,
    which is nth fibonacci number - 1.
    :param M: matrix
    :param expo: exponential power

    """
    if (expo == 0 or expo == 1):        #Base Case
        return M
    elif (expo % 2 == 0):
        return fibPow(matrix_multiplication(M, M), expo//2)     # if expo is even,  M^(n/2) * M^(n/2) = M
    elif (expo % 2 != 0):
        R = fibPow(matrix_multiplication(M, M), expo//2)        # if expo is odd,  M^2 * M = M^3
        return matrix_multiplication(M,R)


def fibo(n):
    """
    Here, we do not find all n terms in the fibonacci series.
    M^(n-1) * Z = W, where W[0][0] has the nth fibonacci number.
    Z = [f(n) = f(1), f(n-1) = f(0)] and W = [f(n+1), f(n)]
    :param n:  position in the fibonacci series

    """
    M = [[1, 1], [1, 0]]
    K = [[1, 0], [0, 0]]
    return matrix_multiplication(fibPow(M, n-1), K)[0][0]   # returns first element in the first column


def matrix_multiplication(A, B):
    u = A[0][0] * B[0][0] + A[0][1] * B[1][0]

    v = A[0][0] * B[0][1] + A[0][1] * B[1][1]

    w = A[1][0] * B[0][0] + A[1][1] * B[1][0]

    x = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    return [[u, v], [w, x]]


def main():
    """
    Main function , takes input n
    and calls the worker functions.

    """
    fibo_input = int(input("Enter a number : "))
    print(fibo(fibo_input))
    print("Time Complexity of fibPow is O(log(n))")

if __name__=='__main__':
    main()