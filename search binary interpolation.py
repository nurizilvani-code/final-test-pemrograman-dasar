# Nuri Zilvani
# D0425008


# Stack Single menggunakan list
class StackSingle:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

# Stack Double
class StackDouble:
    def __init__(self):
        self.stack = []
    
    def push_front(self, item):
        self.stack.insert(0, item)
    
    def push_back(self, item):
        self.stack.append(item)
    
    def pop_front(self):
        if not self.is_empty():
            return self.stack.pop(0)
        return None
    
    def pop_back(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def is_empty(self):
        return len(self.stack) == 0

# Contoh penggunaan
print("=== Stack Single ===")
s = StackSingle()
s.push(15)
s.push(30)
print("Pop:", s.pop())  # 30
print("Peek:", s.peek())  # 15

print("\n=== Stack Double ===")
d = StackDouble()
d.push_front(1)
d.push_back(4)
d.push_front(2)
print("Pop front:", d.pop_front())  # 2
print("Pop back:", d.pop_back())    # 4