class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return(len(self.top))

    def size(self): return(len(self.top))

    def clear(self): self.top = []

    def push (self, item):
        self.top.append(item)

    def pop (self):
        if self.isEmpty():
            return self.top.pop(-1)
    
    def peek (self):
        if not self.isEmpty():
            return self.top[-1]

StackA = Stack()
print(StackA.isEmpty())
StackA.push('핸드폰')
StackA.push('노트북')
print(StackA.size())
StackA.pop()
print(StackA.top)