class Stack:
    def __init__(self):
        self.stack = []      # Main stack to store elements
        self.minStack = []   # Auxiliary stack to store min values
        self.maxStack = []   # Auxiliary stack to store max values

    def push(self, x: int):
        self.stack.append(x)

        # Maintain minStack
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

        # Maintain maxStack
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)
        else:
            self.maxStack.append(self.maxStack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
            self.maxStack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None

    def getMax(self) -> int:
        return self.maxStack[-1] if self.maxStack else None

s = Stack()
s.push(10)
s.push(5)
s.push(11)

print("Smallest: ",s.getMin())  # Output: 1 (smallest element)
print("Biggest: ",s.getMax())  # Output: 10 (largest element)

s.pop()
print("After Pop")
print("Smallest: ",s.getMin())  # Output: 2 (smallest after popping 1)
print("Biggest: ",s.getMax())  # Output: 10 (largest remains)
