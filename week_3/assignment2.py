class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# from Stack import Stack

stack = Stack()

for i in range(10):
    stack.push(i)

while not stack.isEmpty():
    print(stack.pop(), end = " ")
