# ITERATIVE SORTING ALGORITHMS
from random import sample


class Iteration:
    def __init__(self):
        # Initialize empty data list and set max size
        self.data = []
        self.max_size = 100

    def initialise(self):
        # Fill the list with unique random numbers
        self.data = sample(range(1, 3 * self.max_size), self.max_size)

    def print_all(self):
        # Print size and contents of the array
        print("The size of the random array " + str(len(self.data)))
        print("Before sorting, the array is " + str(self.data))

    # Selection sort
    # finds the minimum or maximum in the  unsorted part of the array and moves it to the sorted part. Repeat until the array is fully sorted.
    def selection_sort(self):
        # Iterate through the list
        for i in range(len(self.data) - 1):
            ind_min = i
            # Find index of smallest item in unsorted part
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[ind_min]:
                    ind_min = j
            # Swap smallest with current position
            self.data[ind_min], self.data[i] = self.data[i], self.data[ind_min]
        return self.data

    # Insertion sort
    # takes an element from the unsorted part, finds its correct position in the sorted part, and inserts it. Repeat until the array is fully  sorted.
    def insertion_sort(self):
        for i in range(1, len(self.data)):
            current = self.data[i]
            j = i
            # Shift elements to make space for current
            while j > 0 and current < self.data[j - 1]:
                self.data[j] = self.data[j - 1]
                j -= 1
            self.data[j] = current
        return self.data

    # Bubble sort
    def bubble_sort(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1 - i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data

    # linear search
    def linear_search(self, item):
        for ind in range(len(self.data)):
            if self.data[ind] == item:
                return ind
        raise ValueError(f"{item} not found in the list")

    # binary search - iterative
    def binary_search_iter(self, item):
        start = 0
        end = len(self.data) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.data[mid] < item:
                start = mid + 1
            elif self.data[mid] > item:
                end = mid - 1
            else:
                return mid
        raise ValueError(f"{item} not found in the list")

    # binary search - recursive
    def binary_search_recur(self, item):
        return self._binary_search_recur(self.data, 0, len(self.data) - 1, item)

    def _binary_search_recur(self, arr, start, end, item):
        # arr has to be a sorted array
        if start <= end:
            mid = (start + end) // 2
            if arr[mid] < item:
                return self._binary_search_recur(arr, mid + 1, end, item)
            elif arr[mid] > item:
                return self._binary_search_recur(arr, start, mid - 1, item)
            else:
                return mid
        raise ValueError(f"{item} not found in the list")

    # Ternary Search for a Sorted Array - searching by dividing a sorted array into three equal parts instead of two. Assess and compare its performance with binary searchusing arbitrary sorted arrays.
    def ternary_search(self, item):
        return self._ternary_search(self.data, 0, len(self.data) - 1, item)

    def _ternary_search(self, arr, start, end, item):
        # arr has to be a sorted array
        if start <= end:
            third1 = (end - start) // 3 + start
            if arr[third1] == item:
                return third1
            elif arr[third1] > item:
                return self._ternary_search(arr, start, third1 - 1, item)
            else:
                third2 = (end - start) // 3 + third1
                if arr[third2] == item:
                    return third2
                elif arr[third2] > item:
                    return self._ternary_search(arr, third1 + 1, third2 - 1, item)
                else:
                    return self._ternary_search(arr, third2 + 1, end, item)
        raise ValueError(f"{item} not found in the list")


# Test Selection Sort
arr = Iteration()
arr.initialise()
arr.print_all()
# Test Selection Sort
print("After the selection sort, the array is " + str(arr.selection_sort()))
# Test Insertion Sort
print("After the insertion sort, the array is " + str(arr.insertion_sort()))
# Test Bubble Sort
print("After the bubble sort, the array is " + str(arr.bubble_sort()))

# Test Linear Search
ind = arr.linear_search(5)
print(ind)
print("After the insertion sort, the array is " + str(arr.insertion_sort()))
ind = arr.linear_search(5)
print(ind)


print("After the bubble sort, the array is " + str(arr.bubble_sort()))
ind = arr.binary_search_iter(5)  # Test Binary Search Iterative
print(ind)
ind = arr.binary_search_recur(5)  # Test Binary Search Recursive
print(ind)
ind = arr.ternary_search(5)  # Test Ternary Search
print(ind)
