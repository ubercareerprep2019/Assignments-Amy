# Part 3: Stacks and Queues

# 3A: Stacks


class Stack:
    def __init__(self, elems=[]):
        if elems:
            self.elements = elems
            self.minElement = min(elems)
        else:
            self.elements = []
            self.minElement = None

    def push(self, number: int):
        self.elements.append(number)
        if self.minElement is None or number < self.minElement:  # Update min element
            self.minElement = number

    def pop(self):
        if not self.isEmpty():
            curr = self.elements.pop(len(self.elements) - 1)
            if curr == self.minElement:  # replace min element if we have removed it
                if len(self.elements) >= 1:
                    self.minElement = min(self.elements)
                else:
                    self.minElement = None
            return curr

    def top(self):
        if not self.isEmpty():
            return self.elements[len(self.elements) - 1]

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def min(self):
        return self.minElement


# Stack Test
print("Stack Test")
print("\nCreate empty stack ...")
myStack = Stack()
print("IsEmpty (should be true): " + str(myStack.isEmpty()))
print("Top (should return None, nothing in the stack): " + str(myStack.top()))
print("Min element (should return None): " + str(myStack.min()))

print("Push integers 2, 3, and 1 to the stack ...")
myStack.push(2)
myStack.push(3)
myStack.push(1)

# myStack's elements are [2, 3, 1], three elements
print("IsEmpty (should be false): " + str(myStack.isEmpty()))
print("Min element (should return 1): " + str(myStack.min()))
print("Popping top element (should return 1): " + str(myStack.pop()))

# myStack's elements are [2, 3], two elements
print("Min element (should return 2): " + str(myStack.min()))
print("Top (should return 3): " + str(myStack.top()))
print("Popping top element (should return 3): " + str(myStack.pop()))

# myStack's elements are [2], one element
print("Top (should return 2): " + str(myStack.top()))
print("IsEmpty (should be false): " + str(myStack.isEmpty()))
print("Min element (should return 2): " + str(myStack.min()))
print("Popping top element (should return 2): " + str(myStack.pop()))

# myStack's elements are [], zero elements
print("Popping top element (should return None, stack is empty): " + str(myStack.pop()))
print("Min element (should return None): " + str(myStack.min()))

print("\nCreating new stack with elements, 11, 4, and 7")
myStackNum = Stack([11, 4, 7])
print("IsEmpty (should be false): " + str(myStackNum.isEmpty()))
print("Top (should return 7): " + str(myStackNum.top()))
print("Min element (should return 4): " + str(myStackNum.min()))


# 3B: Queues


class Queue:
    def __init__(self):
        self.eqStack = Stack()
        self.dqStack = Stack()

    def enqueue(self, number: int):
        self.eqStack.push(number)

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


# Queue Test
print("\nQueue Test")
print("\nCreate empty queue ...")
myQueue = Queue()
print("Enqueuing integers 1, 5, and then 7 to the queue ...")
myQueue.enqueue(1)
myQueue.enqueue(5)
myQueue.enqueue(7)

# myQueue's elements are [1, 5, 7]
print("Dequeued element (should return 1): " + str(myQueue.dequeue()))
print("Dequeued element (should return 5): " + str(myQueue.dequeue()))
print("Dequeued element (should return 7): " + str(myQueue.dequeue()))
