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

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence

# Test the function
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_nums = fibonacci(n)
print(fib_nums)
print(f"The first {n} Fibonacci numbers are: {fib_nums}")

