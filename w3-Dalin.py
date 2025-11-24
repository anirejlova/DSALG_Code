# RECURSION AND BACKTRACCKING

from random import sample


# Dev recursive and iterative alg to calc N-th fibonnaci number F(N)
# Fibonacci sequence is defined as F(N+2) = F(N) + F(N+1), with F(1) = F(2) = 1.
# F(1) and F(2) are 0 and 1 respectively.
class Recursion:
    def __init__(self):
        self.data = []
        self.max_size = 100

    def initialise(self):
        # Fill the list with 100 unique random numbers in range 1-300
        self.data = sample(range(1, 3 * self.max_size), self.max_size)

    def print_all(self):
        print("size of random array:", len(self.data))
        print("random array before sorting:", self.data)

    # iterative fibonnaci - n-th number is sum of n-1 and n-2 numbers
    def fib_iter(self, n):
        if n < 1:
            print("ValueError: n must be postive integer")
            # raise ValueError("n must be postive integer")

        f1 = f2 = 1
        out = -1
        if n == 1 or n == 2:
            return 1
        for i in range(3, n + 1):
            out = f1 + f2
            f1 = f2
            f2 = out
            print(f"{str(i)}-th Fibbonaci number is: {str(out)}")
        return out
