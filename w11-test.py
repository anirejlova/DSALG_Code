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
    
    def gcd(self, a, b):  # 2 inputs
        if a == b:
            return a
        elif a < b:  # n is smaller
            return self.gcd(b - a, a)  # recursive call
        else:  # m is smaller
            return self.gcd(a - b, b)  # recursive call
    
#     def palindrome(self, nr): # nr = number of bracket pairs
#         if nr == 0:
#             print("no parentheses to pair")
#         elif nr == 1:
#             print("()")
#         elif nr > 1:
#             left = "("
#             right = ")"
#             
#         else:
#             pass

# run tests
arr = Recursion()
arr.initialise()
# print("GCD of 10 & 35 is: " + str(arr.gcd(10, 35)))
print("GCD of 21 & 49 is: " + str(arr.gcd(21, 49)))

