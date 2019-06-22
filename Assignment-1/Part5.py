# Part 5: Towers of Hanoi

from Part3 import Stack


class TowersOfHanoi:

    def __init__(self, disks: int):
        self.diskCount = disks;
        self.towers = [Stack(), Stack(), Stack()]
        for i in reversed(range(disks)):
            self.towers[0].push(i)  # Add all disks to the first rod

    # Note: The rod indices are 0, 1, and 2
    def moveDisk(self, startingRod: int, destinationRod: int):
        """ Move a disk from the starting rod index to the destination rod index """
        other_rod = (destinationRod + 1) - (startingRod + 1)  # Add one to each index to have the indices start at 1
        other_rod -= 1
        if other_rod < 0:
            other_rod *= -1  # Assure int is positive

        element_to_move = self.towers[startingRod].pop()

        if self.towers[destinationRod].isEmpty() or element_to_move < self.towers[destinationRod].top():
            self.towers[destinationRod].push(element_to_move)
        else:
            # Cannot place a disk on a smaller disk, must place on other rod first
            self.towers[other_rod].push(element_to_move)
            # Try to place disk on destination rod again
            self.moveDisk(other_rod, destinationRod)

    def disksAtRod(self, rodIndex: int):
        """ Returns a list of elements in order at the specified rod index """
        if 0 <= rodIndex <= 2:
            currentStack = self.towers[rodIndex]
            copyStack = Stack()
            tower_list = []
            while not currentStack.isEmpty():  # Flip stack to get list in right order
                elem = currentStack.pop()
                copyStack.push(elem)
            while not copyStack.isEmpty():  # Restore current stack and construct list representation
                elem = copyStack.pop()
                tower_list.append(elem)
                currentStack.push(elem)
            return tower_list
        else:
            # Throw exception if rod index is not in range
            return Exception


# Tests for TowersOfHanoi implementation
def testCreatingEmptyTower():
    t1 = TowersOfHanoi(5)  # Tower 1 starts with discs of size 4, 3, 2, 1, and 0
    assert(t1.disksAtRod(0) == [4, 3, 2, 1, 0])
    assert(t1.disksAtRod(1) == [])
    assert(t1.disksAtRod(2) == [])

    t2 = TowersOfHanoi(3)  # Tower 1 starts with discs of size 2, 1, and 0
    assert (t2.disksAtRod(0) == [2, 1, 0])
    assert (t2.disksAtRod(1) == [])
    assert (t2.disksAtRod(2) == [])

def testLegalDiskMove():
    t = TowersOfHanoi(3)  # Tower 1 starts with discs of size 2, 1, and 0
    t.moveDisk(0, 2)
    assert (t.disksAtRod(0) == [2, 1])
    assert (t.disksAtRod(1) == [])
    assert (t.disksAtRod(2) == [0])

def testNonLegalDiskMove():
    # Not working, I am not handling the what to do when a disc does not fit on the destination rod correctly.
    t = TowersOfHanoi(3)  # Tower 1 starts with discs of size 2, 1, and 0
    t.moveDisk(0, 2)
    t.moveDisk(0, 2)
    assert (t.disksAtRod(0) in [2])
    assert (t.disksAtRod(1) == [1])
    assert (t.disksAtRod(2) == [0])
