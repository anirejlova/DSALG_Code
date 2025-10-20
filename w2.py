# ITERATIVE SORTING ALGORITHMS
import random


class Iteration:
    def __init__(self):
        # Initialize empty data list and set max size
        self.items = []
        self.max_size = 50

    def initialise(self):
        # Fill the list with unique random numbers
        for i in range(1, self.max_size + 1):
            data = random.randint(1, 3 * self.max_size)  # 1-300 int range
            self.items.append(data)

    def print_all(self):
        # Print size and contents of the array
        print("The size of the random array " + str(len(self.items)))
        print("Before sorting, the array is " + str(self.items))

    # Selection sort
    # finds the minimum or maximum in the unsorted part of the array and moves it to the sorted part. Repeat until the array is fully sorted.
    def selection(self):
        for i in range(
            len(self.items) - 1
        ):  # iterate through the list, take the current position and think it as minimum
            min = i
            for j in range(
                i + 1, len(self.items)
            ):  # iterate through the list "again", take the next value from the "unsorted" part, do it for all unsorted part
                if (
                    self.items[j] < self.items[min]
                ):  # if the next value is smaller than the current minimum, change the minimum
                    min = j
            # Swap found smallest with current position
            self.items[min], self.items[i] = self.items[i], self.items[min]
        return self.items

    # Insertion sort
    # takes an element from the unsorted part, finds its correct position in the sorted part, and inserts it. Repeat until the array is fully  sorted.
    def insertion(self):
        for i in range(1, len(self.items)):
            current = self.items[i]  # save the next element from the unsorted part
            j = i - 1  # set j as one position before i
            while (
                j >= 0 and current < self.items[j]
            ):  # if/while j is not negative and greater than current
                self.items[j + 1] = self.items[
                    j
                ]  # shift the item at position j to the right
                j -= 1  # move j one position to the left
            self.items[j + 1] = current  # insert current after the new position of j
        return self.items
        """Example (i=1) with [3, 1, 2]:
            current = 1
            shift: [3, 3, 2] (3 moved right)
            j becomes -1 so loop stops
            you must do self.items[0] = current → [1, 3, 2]
            Without that assignment the array stays [3, 3, 2] and 1 is lost."""

    # Bubble sort
    # compares adjacent elements in the unsorted part and swaps them if needed. After each pass, the last element of the unsorted part is in its final position. Repeat until the array is fully sorted. -- compare two and swap if needed, simple
    def bubble(self):
        for i in range(len(self.items) - 1):  # number of passes
            for j in range(len(self.items) - 1 - i):  # last i elements already sorted
                if (
                    self.items[j] > self.items[j + 1]
                ):  # if the left element is greater than the right one, swap them
                    self.items[j], self.items[j + 1] = self.items[j + 1], self.items[j]
        return self.items

    # Linear Search for an Array or List - sequentially checking each element of the array or list to find a target value
    def linear_search(self, target):
        print("Target value to find: " + str(target))
        for i in range(len(self.items)):
            if self.items[i] == target:
                return i
        raise ValueError(f"{target} not found in the list")

    # Binary Search for a Sorted Array (Iterative Method) - halving the search space at each step.
    def binary_search(self, target):
        print("Target value to find: " + str(target))
        low = 0  # first index
        high = len(self.items) - 1  # last index

        while low <= high:  # while there is still a search space
            mid = (low + high) // 2  # find the middle index
            if self.items[mid] < target:  # target is greater than mid value
                low = mid + 1  # search in the right half
            elif self.items[mid] > target:  # target is less than mid value
                high = mid - 1  # search in the left half
            else:
                return mid  # target found
        raise ValueError(f"{target} not found in the list")


# run
arr = Iteration()
arr.initialise()
arr.print_all()
print()
# Sorting tests
print("After the selection sort, the array is " + str(arr.selection()))
print("After the insertion sort, the array is " + str(arr.insertion()))
print("After the bubble sort, the array is " + str(arr.bubble()))

print()
# Searching test - unsorted array
print(
    "Value first found at index: " + str(arr.linear_search(9))
)  # diff values each time due to randint
print("Value first found at index: " + str(arr.binary_search(9)))
