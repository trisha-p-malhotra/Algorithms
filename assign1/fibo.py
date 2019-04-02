import time

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def main():
    n = 32
    start = time.time()
    result = (fibo(n))
    end = time.time()
    print("Fibonacci Series :  Value at position " + str(n) + " is :")
    print(result)
    print("Time taken in seconds:")
    print(end - start)

    """
    ANSWER : 
         29 to 32 it gets progressively worse
         32 is the first value tht takes more than 1 second., 
         all lower values of n take less than 1 second to compute !
    """



if __name__ == '__main__':
    main()