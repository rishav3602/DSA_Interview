class Stack:
    def __init__(self):
        self.stack = []

    def push(self, obj):
        self.stack.append(obj)
        print(f"This item: {obj} is added to the stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the given stack.")
            return item
        else:
            print("Stack is empty. Cannot perform pop operation.")
            return None

    def peek(self):
        if not self.is_empty():
            item = self.stack[-1]
            print(f"{item} is present at the top of the stack.")
            return item
        else:
            print("Stack is empty. Cannot perform peek operation.")
            return None

    def is_empty(self):
        return len(self.stack) == 0
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
# stack.pop()
stack.peek()

