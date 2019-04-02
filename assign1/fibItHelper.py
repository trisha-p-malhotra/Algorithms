import time


def fibItHelper(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibItHelper(n-1, b, a+b)


def fibIt():
    n = 32
    start = time.time()
    result = fibItHelper(n, 0, 1)
    end = time.time()
    print(result)
    print(end - start)

    """
    ANSWER :
        No,fibIt does Not run slowly on the value of n 
        that made fib run slowly'
        the maximum possible value of n = 997 takes 0.0025 seconds,
        which is extremely faster than fib function, 
        where 32 value itself took more than 1.00 second.
    """

fibIt()