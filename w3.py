from random import sample

class Recursion:
    def __init__(self):
        self.items = []
        self.max_size = 100
        
    def initil(self):
        self.items = sample(range(0,2*self.max_size), self.max_size)
        
    def get_items(self):
        return self.items
    
    def lenght(self):
        return len(self.items)
    
    def __str__(self):
        return f"Size of array: {self.lenght()}; \n Array before sorting: {self.get_items()}"
    
    def fibonacci(self):
        

# run
arr = Recursion()
arr.initil()
print(arr)