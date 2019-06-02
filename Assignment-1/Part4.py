# Part 4: Linked Lists


class Node(object):
    def __init__(self, val=None, nxt=None):
        self.value = val
        self.nextNode = nxt


class SinglyLinkedList:
    def __init__(self):
        # self.nodes = []
        self.head = None
        self.tail = None
        self.length = 0

    def pushBack(self, data: int):
        """ Add a single node containing data to the end of the list """
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.nextNode = new_node
        self.length += 1
        self.tail = new_node

    def popBack(self) -> Node:
        """ Removes a single node from the end of the list """
        last_node = None
        if self.size() == 1:
            last_node = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.length > 1:
            penultimate_node = self.elementAt(self.length - 2)
            penultimate_node.nextNode = None
            last_node = self.tail
            self.tail = penultimate_node
            self.length -= 1
        return last_node

    def insert(self, index: int, data: int):
        """ Adds a single node containing data to a chosen location in the list. If the index is above the size of
        the list, do nothing """
        if self.length > index >= 0:
            new_node = Node(data)
            if index == 0:
                curr_head = self.head
                self.head = new_node
                self.head.nextNode = curr_head
            elif index == 1:
                second_node = self.head.nextNode
                self.head.nextNode = new_node
                new_node.nextNode = second_node
            else:
                prev_curr_node = self.elementAt(index - 1)
                curr_node = prev_curr_node.nextNode
                prev_curr_node.nextNode = new_node
                new_node.nextNode = curr_node
            if index == self.length - 1:  # if added at the end of list, update the tail
                self.tail = new_node
            self.length += 1

    def erase(self, index: int):
        """ Erases a single node at the index location in the list """
        if self.length > index >= 0:
            if index == 0:
                self.head = self.head.nextNode
                if self.length == 1:
                    self.tail = None  # set tail to none if no more nodes in list
            elif index == 1:
                self.head.nextNode = self.head.nextNode.nextNode
                if self.length == 2:
                    self.tail = self.head  # update tail if it was erased
            else:
                prev_node = self.elementAt(index - 1)
                curr_node = prev_node.nextNode
                prev_node.nextNode = curr_node.nextNode
            self.length -= 1

    def elementAt(self, index) -> Node:
        """ Returns a single node at the index location in the list """
        if self.length > index >= 0:
            currNode = self.head
            while currNode is not None and index > 0:
                currNode = currNode.nextNode
                index -= 1
            return currNode
        else:
            return None  # index out of range

    def size(self):
        """ Returns the length of the list """
        return self.length

    def hasCycle(self):
        """ Returns a bool if a cycle is detected in the list. A cycle is when node references an earlier node in the
            'next' reference """
        isCycle = False
        currNode = self.head
        unique_nodes = [currNode]
        while currNode is not None:
            if currNode in unique_nodes:
                isCycle = True
                break
            else:
                unique_nodes.append(currNode)
                currNode = currNode.nextNode
        return isCycle

# Tests for SinglyLinkedList implementation
def testPushBackAddsOneNode():
    my_list = SinglyLinkedList()
    my_list.pushBack(7)
    assert(my_list.size() == 1)
    first_node = my_list.elementAt(0)
    assert(first_node.value == 7)
    assert(first_node.nextNode is None)
    assert(my_list.head == first_node)
    assert(my_list.tail == first_node)


def testPopBackRemovesCorrectNode():
    # Create a linked list with 3 elements
    my_list = SinglyLinkedList()
    my_list.pushBack(1)
    my_list.pushBack(2)
    my_list.pushBack(3)
    assert(my_list.tail == my_list.elementAt(2))

    # Remove the third element in the linked list
    removed_node = my_list.popBack()
    assert(my_list.size() == 2)
    assert(removed_node.value == 3)
    assert(my_list.elementAt(1).nextNode is None)
    assert(my_list.tail == my_list.elementAt(1))

    # Remove the second element in the linked list
    removed_node = my_list.popBack()
    assert(my_list.size() == 1)
    assert(removed_node.value == 2)
    assert(my_list.elementAt(0).nextNode is None)
    assert(my_list.tail == my_list.elementAt(0))
    assert(my_list.tail == my_list.head)

    # Remove the last element in the linked list
    removed_node = my_list.popBack()
    assert(my_list.size() == 0)
    assert(removed_node.value == 1)
    assert(my_list.head is None)
    assert(my_list.tail is None)


def testEraseRemovesCorrectNode():
    # Create a linked list with 2 elements
    my_list = SinglyLinkedList()
    my_list.pushBack(2)
    my_list.pushBack(5)
    my_list.pushBack(8)

    # Erase the middle element
    my_list.erase(1)
    assert(my_list.size() == 2)
    assert(my_list.head.nextNode == my_list.tail)

    # Erase the first element when there are 2 elements
    my_list.erase(0)
    assert(my_list.size() == 1)
    assert(my_list.head.value == 8)
    assert(my_list.tail.value == 8)

    # Erase the last and only element
    my_list.erase(0)
    assert(my_list.size() == 0)
    assert(my_list.head == None)
    assert(my_list.tail == None)


def testEraseDoesNothingIfNoNode():
    # Create a linked list with no elements
    my_list = SinglyLinkedList()

    # Attempt to erase an non existing element
    my_list.erase(0)
    assert(my_list.size() == 0)
    my_list.erase(-2)
    assert (my_list.size() == 0)

    # Add elements and erase non a existing element
    my_list.pushBack(1)
    my_list.pushBack(3)
    my_list.erase(3)
    assert(my_list.size() == 2)
    assert(my_list.head.value == 1)
    assert(my_list.tail.value == 3)


def testElementAtReturnNode():
    # Create a linked list with 3 elements
    my_list = SinglyLinkedList()
    my_list.pushBack(1)
    my_list.pushBack(2)
    my_list.pushBack(3)

    # Grab the first element
    first_node = my_list.elementAt(0)
    assert(first_node.value == 1)
    assert(first_node.nextNode.value == 2)

    # Grab the middle element
    mid_node = my_list.elementAt(1)
    assert (mid_node.value == 2)
    assert (mid_node.nextNode.value == 3)

    # Grab the last element
    last_node = my_list.elementAt(2)
    assert(last_node.value == 3)
    assert(last_node.nextNode is None)


def testElementAtReturnsNoNodeIfIndexDoesNotExist():
    # Create a linked list with no elements
    my_list = SinglyLinkedList()
    assert(my_list.elementAt(0) is None)

    # Add elements and try to grab a node at a index that does not exist
    my_list.pushBack(3)
    my_list.pushBack(5)
    assert(my_list.elementAt(3) is None)
    assert(my_list.elementAt(-1) is None)
    assert(my_list.elementAt(5) is None)


def testSizeReturnsCorrectSize():
    # Create a linked list with no elements
    my_list = SinglyLinkedList()
    assert(my_list.size() == 0)

    # Add nodes to list with push back function
    my_list.pushBack(1)
    my_list.pushBack(1)
    assert(my_list.size() == 2)

    # Add node to list with insert function
    my_list.insert(0, 5)
    my_list.insert(1, 5)
    my_list.insert(2, 5)
    assert(my_list.size() == 5)

    # Remove nodes from list with pop back function
    my_list.popBack()
    my_list.popBack()
    assert(my_list.size() == 3)

    # Remove nodes from list with erase function
    my_list.erase(2)
    my_list.erase(1)
    my_list.erase(0)
    assert(my_list.size() == 0)

def isPalindrome(linkedList: SinglyLinkedList):
    """ Returns a bool if a linked list is a palindrome """
    is_palindrome = True
    num_matches = linkedList.size() // 2
    frontPtr = 0
    backPtr = linkedList.size() - 1
    for _ in num_matches:
        if linkedList.elementAt(frontPtr).value != linkedList.elementAt(backPtr).value:
            is_palindrome = False
            break
        else:
            frontPtr += 1
            backPtr -= 1
    return is_palindrome
