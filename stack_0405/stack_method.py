top = []
def isEmpty():
    return len(top) == 0

def push(item):
    top.append(item)

def pop():
    if not isEmpty():
        return top.pop(-1)
    
def peek():
    if not isEmpty():
        return top[-1]
    
def size(): return len(top)

def clear():
    global top
    top = []

print(isEmpty())
push('핸드폰')
push('노트북')
push('핸드폰')
pop()
print(top)


