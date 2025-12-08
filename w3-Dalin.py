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

    # recursive fibonnaci - inputs > 2, output is the sum of two prevous outputs
    # recursion stops when input is 1 or 2 - output being 1 for these cases
    def fib_recur(self, n):
        if n < 1:
            print("ValueError: n must be postive integer")
            # raise ValueError("n must be postive integer")
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib_recur(n - 1) + self.fib_recur(n - 2)

    # find the greatest common divisor (GCD) of 2 positive integers
    # If ints equal, GCD is that number
    # otherwise, GCD is GCD of smaller number and the positive difference of the two ints
    def gcd(self, n, m):  # 2 inputs
        if n == m:
            return n
        elif n < m:  # n is smaller
            return self.gcd(m - n, n)  # recursive call
        else:  # m is smaller
            return self.gcd(n - m, m)  # recursive call

    # Merge sort implementation
    # Merge Sort divides the array into halves recursively until each part has at most one element. Then merges the sorted halves into a single sorted array until there is only one sorted group.
    def merge_sort(self):
        # arr has to be sorted array
        self._merge_sort(
            self.data, 0, len(self.data) - 1
        )  # helper function - (array to be sorted, left (start) & right(length) boundaries)
        print("After the merge sort: ", str(self.data))

    def _merge_sort(self, arr, start, end):
        if start >= end:
            return  # base case - array of 1 or less elements is already sorted
        mid = (
            start + end
        ) // 2  # alternatively:  (end- start) // 2 + start, because of int overflow in other languages
        self._merge_sort(arr, start, mid)  # sort left half
        self._merge_sort(arr, mid + 1, end)  # sort right half
        self._merge(arr, start, mid, end)  # merge sorted halves

    def _merge(self, arr, start, mid, end):
        temp = []  # temporary array to hold merged result
        left = start  # starting index for left subarray
        right = mid + 1  # starting index for right subarray

        # compare the first elements of each subarray, the smaller one is inserted first
        while left <= mid and right <= end:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # when one subarray is exhausted, append the remaining elements of the other subarray
        # only one of these loops will execute
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= end:
            temp.append(arr[right])
            right += 1

        # upfate original array with merged result
        for i in range(len(temp)):
            arr[start + i] = temp[i]


# run test
arr = Recursion()
arr.initialise()
arr.fib_iter(10)
print("Recursive Fibbonaci number: ", arr.fib_recur(10))

# test GCD
print("GCD of 27 & 18 is: " + str(arr.gcd(27, 18)))
print("GCD of 28 & 19 is: " + str(arr.gcd(28, 19)))

# test merge sort
arr.initialise()
arr.print_all()
arr.merge_sort()
