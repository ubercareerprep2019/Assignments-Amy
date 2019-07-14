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


# Representing a hierarchical structure using a tree

# Exercise 2: Printing a tree level by level
class Employee(object):
    def __init__(self, name, title, direct_reports):
        self.name = name
        self.title = title
        self.directReports = direct_reports

    def print_info(self):
        output = ""
        if self.name:
            output += "Name: " + self.name
        if self.title:
            if output != "":
                output += ", "
            output += "Title: " + self.title
        print(output)


class OrganizationStructure(object):
    def __init__(self, ceo):
        self.ceo = ceo

    def print_level_by_level(self):
        nodes_to_print = Queue()
        nodes_to_print.enqueue(self.ceo)
        new_level = Employee(None, None, None)
        nodes_to_print.enqueue(new_level)

        while not nodes_to_print.isEmpty():  # Dequeue node
            employee = nodes_to_print.dequeue()
            if employee is not None:
                employee.print_info()
                # Add the dequeued node's children (if they exist) to the queue
                if employee.directReports is not None:
                    for report in employee.directReports:
                        if report is not None:
                            nodes_to_print.enqueue(report)
                if employee == new_level and not nodes_to_print.isEmpty():
                    nodes_to_print.enqueue(new_level)  # Add space if we reached current end of level (and not the tree)

    # Exercise 3: Printing the number of levels
    def print_num_levels(self):
        level_count = 0
        if self.ceo is not None:
            nodes_to_check = Queue()
            nodes_to_check.enqueue(self.ceo)
            level_count += 1
            new_level = Employee(None, None, None)
            nodes_to_check.enqueue(new_level)

            while not nodes_to_check.isEmpty():  # Dequeue node
                employee = nodes_to_check.dequeue()
                if employee is not None:
                    # Add the dequeued node's children (if they exist) to the queue
                    if employee.directReports is not None:
                        for report in employee.directReports:
                            if report is not None:
                                nodes_to_check.enqueue(report)
                    if employee == new_level and not nodes_to_check.isEmpty():
                        nodes_to_check.enqueue(new_level)  # Add space if we reached current end of level
                        level_count += 1
        print(level_count)


def sample_org_tree_1():
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
    return OrganizationStructure(a)


def sample_org_tree_2():
    i = Employee("I", "Director", None)
    b = Employee("B", "CFO", [i])
    f = Employee("F", "Engineer", None)
    g = Employee("G", "Engineer", None)
    h = Employee("H", "Engineer", None)
    d = Employee("D", "Manager", [f, g, h])
    e = Employee("E", "Manager", None)
    c = Employee("C", "CTO", [d, e])
    a = Employee("A", "CEO", [b, c])
    return OrganizationStructure(a)


# Exercise Methods
def exercise1():
    left_child = TreeNode(6, None, None)
    right_child = TreeNode(3, None, None)
    left = TreeNode(7, None, None)
    right = TreeNode(17, left_child, right_child)
    root = TreeNode(1, left, right)
    current_tree = Tree(root)
    current_tree.print_tree()


def exercise2():
    org = sample_org_tree_1()
    org.print_level_by_level()


def exercise3():
    org_1 = sample_org_tree_1()
    org_1.print_num_levels()

    org_2 = sample_org_tree_2()
    org_2.print_num_levels()


if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
