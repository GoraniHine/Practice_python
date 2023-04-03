#%%
class set:
    def __init__(self):
        self.items = []

    def display(self, msg):
        print(msg, self.items)

    def size(self):
        return len(self.items)
    
    def contains(self, elem):
        return elem in self.items
    
    def insert(self, elem):
        self.items.append(elem)

    def delete(self, elem):
        self.items.remove(elem)

    def equals(self, setB):
        if self.size() != setB.size():
            return False
        for elem in self.items:
            if elem in setB:
                return False
        return True
    
    def union(self, setB):
        setC = set()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC

setA = set()
setA.insert('휴대폰')
setA.insert('빗')
setA.insert('지갑')
setA.display('집합 A: ')

setB = set()
setB.insert('빗')
setB.insert('야구공')
setB.insert('지갑')
setB.display('집합 B: ')

setC = setA.union(setB)
setC.display('집합 C: ')
