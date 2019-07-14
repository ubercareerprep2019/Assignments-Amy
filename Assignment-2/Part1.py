# Part 1: Trees (Exercise 1-3)

from common import Queue

# Exercise 1: Printing a Tree
class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self, root):
        self.root = root

    """ Print entire tree from tree root """
    def print_tree(self):
        self.print_tree_helper(self.root)

    def print_tree_helper(self, root):
        print(root.data)
        if root.left:
            self.print_tree_helper(root.left)
        if root.right:
            self.print_tree_helper(root.right)

def excercise1():
    leftChild = TreeNode(6, None, None)
    rightChild = TreeNode(3, None, None)
    left = TreeNode(7, None, None)
    right = TreeNode(17, leftChild, rightChild)
    root = TreeNode(1, left, right)
    currentTree = Tree(root)
    currentTree.print_tree()


# Representing a hierarchical structure using a tree

# Exercise 2: Printing a tree level by level
class OrganizationStructure(object):
    def __init__(self, ceo):
        self.ceo = ceo

    def print_level_by_level(self):
        nodes_to_print = Queue()
        nodes_to_print.enqueue(self.ceo)
        newLevel = Employee(None, None, None)
        nodes_to_print.enqueue(newLevel)

        while not nodes_to_print.isEmpty():  # Dequeue node
            employee = nodes_to_print.dequeue()
            if employee is not None:
                employee.print_info()
                # Add the dequeued node's children (if they exist) to the queue
                if employee.directReports is not None:
                    for report in employee.directReports:
                        if report is not None:
                            nodes_to_print.enqueue(report)
                if employee == newLevel and not nodes_to_print.isEmpty():
                    nodes_to_print.enqueue(newLevel)  # Add space if we reached current end of level (and not the tree)


class Employee(object):
    def __init__(self, name, title, directReports):
        self.name = name
        self.title = title
        self.directReports = directReports

    def print_info(self):
        output = ""
        if self.name:
            output += "Name: " + self.name
        if self.title:
            if output != "":
                output += ", "
            output += "Title: " + self.title
        print(output)

def excercise2():
    # Set up sample org structure
    k = Employee("K", "Sales Intern", None)
    j = Employee("J", "Sales Representative", [k])
    i = Employee("I", "Director", [j])
    b = Employee("B", "CFO", [i])
    f = Employee("F", "Engineer", None)
    g = Employee("G", "Engineer", None)
    h = Employee("H", "Engineer", None)
    d = Employee("D", "Manager", [f, g, h])
    e = Employee("E", "Manager", None)
    c = Employee("C", "CTO", [d, e])
    a = Employee("A", "CEO", [b, c])

    org = OrganizationStructure(a)
    org.print_level_by_level()


if __name__ == "__main__":
    excercise1()
    excercise2()