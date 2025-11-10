# assesment 1, 20/10/2025
class Iteration:
    def __init__(self):
        # Initialize data list
        self.items = [12,5,19,3,14,9,7,18,2]
        
    # Insertion sort
    # takes an element from the unsorted part, finds its correct position in the sorted part, and inserts it. Repeat until the array is fully  sorted.
    def insertion(self):
        for i in range(1, len(self.items)):
            current = self.items[i]  # save the next element from the unsorted part
            j = i - 1  
            while (
                j >= 0 and current < self.items[j]
            ):  # if/while j is not negative and greater than current
                self.items[j + 1] = self.items[j]  # shift the item at position j to the right
                j -= 1  # move j one position to the left
            self.items[j + 1] = current  # insert current after the new position of j
            print(f"Iteration {i}: " + str(self.items))
        return self.items

    # Binary Search for a Sorted Array (Iterative Method) - halving the search space at each step.
    def binary_search(self, target):
        print("Target value to find: " + str(target))
        low = 0  # first index
        high = len(self.items) - 1  # last index

        while low <= high:  # while there is still a search space
            mid = (low + high) // 2  # find the middle index 
            if self.items[mid] <= target:  # target is greater than mid value
                return self.items[mid], mid            
            elif self.items[mid] > target:  # target is less than mid value
                high = mid - 1  # search in the left half
            else:
                return -1

    def __str__(self):
        return f"Size of array: {len(self.items)};\n Array before sorting: {self.items}"

class Stack:
    def __init__(self):
        self.items = []

    # Add an element to the top of the stack
    def push(self, item):
        self.items.append(item)

    #  Remove the element from the top of the stack
    def pop(self):
        return self.items.pop(-1)

    # View the element at the top of the stack without removing it
    def peek_head(self):
        return self.items[-1]

    # Return the number of elements in the stack
    def length(self):
        return len(self.items)
    
    def bracket_check(self, input_str):
        print("\nThe input string is: ", input_str)
        pairs = {")": "("}
        count = 0
        for character in input_str:
            if character in pairs.values():
                self.push(character)
            elif character in pairs:
                self.pop()
                count += 1
        return count*2

    
# run
arr = Iteration()
print(arr)
print("After the insertion sort, the array is " + str(arr.insertion()))

target_value = 6
el, ind = arr.binary_search(target_value)
print(f"Target: {target_value}; Element: {el}; Index: {ind}")

s = Stack()
print(s.bracket_check("((()())))"))
