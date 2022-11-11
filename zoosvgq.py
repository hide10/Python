class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


str_stack = Stack()
for c in "Yesterday":
    str_stack.push(c)

reverse = ""

while str_stack.size():
    reverse += str_stack.pop()

print(reverse)

list1 = [1,2,3,4,5]
list2 = []

num_stack = Stack()
for item in list1:
    num_stack.push(item)

while not num_stack.is_empty():
    list2.append(num_stack.pop()+1)

print(list2)
