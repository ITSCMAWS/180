# This is a python program to calculate the Fibonacci sequence.  Create the python code below to do this.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter a number: "))
print(fib(n))
