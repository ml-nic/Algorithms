class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()


if __name__ == "__main__":
    stack = Stack()

    for element in "h-el--lo --wo-r--l-d-":
        if element != "-":
            stack.push(element)
    print(stack.items)
    print(stack.size())
    for i in range(len("hello world")):
        stack.pop()
    print(stack.size())
