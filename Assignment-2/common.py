class Stack:
    def __init__(self, elems=[]):
        if elems:
            self.elements = elems
        else:
            self.elements = []

    def push(self, obj):
        self.elements.append(obj)

    def pop(self):
        if not self.isEmpty():
            curr = self.elements.pop(len(self.elements) - 1)
            return curr
        else:
            return Exception  # Throw an exception if try to pop an empty stack

    def top(self):
        if not self.isEmpty():
            return self.elements[len(self.elements) - 1]

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.eqStack = Stack()
        self.dqStack = Stack()

    def enqueue(self, obj):
        self.eqStack.push(obj)

    def dequeue(self):
        if self.dqStack.isEmpty():
            if self.eqStack.isEmpty():
                return None  # no elements in queue, nothing to dequeue
            else:
                # nothing on dequeue stack, move all from enqueue stack to dequeue stack
                while not self.eqStack.isEmpty():
                    curr = self.eqStack.pop()
                    self.dqStack.push(curr)
        return self.dqStack.pop()

    def isEmpty(self):
        return self.eqStack.isEmpty() and self.dqStack.isEmpty()
