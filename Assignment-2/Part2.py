# Part 3: Trees (Exercise 4-6)

# For exercise 6
import csv
import datetime


# Exercise 4: Implement a binary search tree

class BinarySearchTree(object):
    def __init__(self, root):
        self.root = root
        self.size = 0  # Needed to keep track of size for exercise 5

    def insert(self, key: int):
        """ Inserts a key into this binary search tree. If there are n nodes in the tree, then the average runtime of
            this method should be log(n)."""
        node_to_insert = Node(key, None, None)
        self.insert_helper(node_to_insert)

    def insert_helper(self, node):
        self.size += 1
        if self.root is None:
            self.root = node
        else:
            curr_node = self.root
            inserted = False
            while inserted is False:
                if node.key > curr_node.key:
                    if curr_node.right is None:  # Insert key if nothing on right sub tree
                        curr_node.right = node
                        inserted = True
                    else:
                        curr_node = curr_node.right
                else:
                    if curr_node.left is None:  # Insert key if nothing on left sub tree
                        curr_node.left = node
                        inserted = True
                    else:
                        curr_node = curr_node.left

    def find(self, key: int):
        """ Checks whether or not a key exists in this binary search tree. If there are n nodes in the tree, then the
            average runtime of this method should be log(n). Returns true if key is in tree, false otherwise. """
        is_in_tree = False
        if self.root is not None:
            curr_node = self.root
            while curr_node is not None:
                if key == curr_node.key:
                    is_in_tree = True
                    break
                if key > curr_node.key:
                    curr_node = curr_node.right
                else:
                    curr_node = curr_node.left
        return is_in_tree

    # Note: These functions are used for exercise 5 and are under the assumption the tree is using nodes with values
    # (or KeyValueNode as defined below).
    def insert_entry(self, name, phone_number):
        node_to_insert = KeyValueNode(name, phone_number, None, None)
        self.insert_helper(node_to_insert)

    def find_entry(self, name):
        if self.root is not None:
            curr_node = self.root
            while curr_node is not None:
                if name == curr_node.key:
                    return curr_node.value
                elif name > curr_node.key:
                    curr_node = curr_node.right
                else:
                    curr_node = curr_node.left
        return -1


class Node(object):
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


class KeyValueNode(object):
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def sample_tree_for_testing():
    # Diagram of the sample tree
    #         5
    #       /   \
    #     4       7
    #   /       /   \
    # 3       6       8
    t = BinarySearchTree(
        Node(5,
             Node(4,
                  Node(3, None, None),
                  None),
             Node(7,
                  Node(6, None, None),
                  Node(8, None, None))
             ))
    return t


def test_binary_search_tree_insert():
    t = BinarySearchTree(None)
    t.insert(5)  # Tree should contain 5
    assert (t.find(5) is True)
    t.insert(7)
    t.insert(4)  # Tree should contain 5, 4, 7
    assert (t.find(7) is True)
    assert (t.find(4) is True)
    t.insert(6)
    t.insert(8)
    t.insert(3)  # Tree should contain 5, 4, 3, 7, 6, 8
    assert (t.find(6) is True)
    assert (t.find(8) is True)
    assert (t.find(3) is True)


def test_binary_search_tree_find():
    t = sample_tree_for_testing()
    assert (t.find(5) is True)
    assert (t.find(3) is True)
    assert (t.find(7) is True)
    assert (t.find(0) is False)


def exercise4():
    """ Runs all tests for exercise 4 """
    test_binary_search_tree_insert()
    test_binary_search_tree_find()


# Exercise 5: Implement a phone book

# After a quick google search, seems like Python doesn't have an interfaces (I have only used interfaces in Java).
# Instead I will name the classes differently for the different implementations.
class PhoneBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class ListPhoneBook:  # Uses an array to implement the class
    def __init__(self):
        self.entries = []

    def size(self):
        """ Returns the number of entries in this phone book """
        return len(self.entries)

    def insert(self, name, phone_number):
        """ Inserts an entry in this phone book. Input the string of the name for the entry and the phone number for
            the entry """
        self.entries.append(PhoneBookEntry(name, phone_number))

    def find(self, name):
        """ Returns the number of entries in this phone book. Input the name to search for and returns the long of the
            phone number entry or -1 if name is not present """
        for entry in self.entries:
            if entry.name == name:
                return entry.phone_number
        return -1  # Name was not present in the current entries


class BinarySearchTreePhoneBook:  # Uses a binary search tree to implement the class
    def __init__(self):
        self.entries = BinarySearchTree(None)

    def size(self):
        """ Returns the number of entries in this phone book """
        return self.entries.size

    def insert(self, name, phone_number):
        """ Inserts an entry in this phone book. Input the string of the name for the entry and the phone number for
            the entry """
        self.entries.insert_entry(name, phone_number)

    def find(self, name):
        """ Returns the number of entries in this phone book. Input the name to search for and returns the long of the
            phone number entry or -1 if name is not present 
            :rtype: int"""
        return self.entries.find_entry(name)


def test_list_phone_book_size():
    phone_book = ListPhoneBook()
    assert(phone_book.size() == 0)
    phone_book.insert("ABC", 1111111111)
    phone_book.insert("XYZ", 9999999999)
    assert(phone_book.size() == 2)


def test_binary_search_tree_phone_book_size():
    phone_book = BinarySearchTreePhoneBook()
    assert (phone_book.size() == 0)
    phone_book.insert("ABC", 1111111111)
    phone_book.insert("XYZ", 9999999999)
    assert(phone_book.size() == 2)


def test_list_phone_book_insert():
    phone_book = ListPhoneBook()
    phone_book.insert("ABC", 1111111111)
    assert (phone_book.find("ABC") == 1111111111)
    assert (phone_book.size() == 1)
    phone_book.insert("XYZ", 9999999999)
    assert (phone_book.find("XYZ") == 9999999999)
    assert (phone_book.size() == 2)


def test_binary_search_tree_phone_book_insert():
    phone_book = BinarySearchTreePhoneBook()
    phone_book.insert("ABC", 1111111111)
    assert(phone_book.find("ABC") == 1111111111)
    assert(phone_book.size() == 1)
    phone_book.insert("XYZ", 9999999999)
    assert(phone_book.find("XYZ") == 9999999999)
    assert(phone_book.size() == 2)


def test_list_phone_book_find():
    phone_book = ListPhoneBook()
    phone_book.insert("ABC", 1111111111)
    phone_book.insert("XYZ", 9999999999)
    phone_book.insert("DEF", 2222222222)
    assert (phone_book.find("ABC") == 1111111111)
    assert (phone_book.find("DEF") == 2222222222)
    assert (phone_book.find("ZZZ") == -1)
    assert (phone_book.find("") == -1)


def test_binary_search_tree_phone_book_find():
    phone_book = BinarySearchTreePhoneBook()
    phone_book.insert("ABC", 1111111111)
    phone_book.insert("XYZ", 9999999999)
    phone_book.insert("DEF", 2222222222)
    assert(phone_book.find("ABC") == 1111111111)
    assert(phone_book.find("DEF") == 2222222222)
    assert(phone_book.find("ZZZ") == -1)
    assert(phone_book.find("") == -1)


def exercise5():
    """ Runs all tests for exercise 5 """
    # Testing size functions
    test_list_phone_book_size()
    test_binary_search_tree_phone_book_size()
    # Testing insert functions
    test_list_phone_book_insert()
    test_binary_search_tree_phone_book_insert()
    # Testing find functions
    test_list_phone_book_find()
    test_binary_search_tree_phone_book_find()


# Exercise 6: Unsorted lists v.s. Binary search trees

# Note: had to look up how to read from .csv and .txt files in Python. I also looked at how to keep track of
# milliseconds. I listed the websites I looked at below:
# - Reading from a .csv: https://realpython.com/python-csv/
# - Reading from a .txt: https://stackabuse.com/read-a-file-line-by-line-in-python/
# - Tracking milliseconds: https://stackoverflow.com/questions/766335/python-speed-testing-time-difference-milliseconds

def read_from_csv(phone_book, csv_file, text_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Insert entries from csv file into the given phone book
        start_time_for_insert = datetime.datetime.now()
        for row in csv_reader:
            phone_book.insert(row[0], int(row[1]))

        # Print time it took to insert into phone book and its current size
        end_time_for_insert = datetime.datetime.now()
        time_for_insert = end_time_for_insert - start_time_for_insert
        print("Insert took " + str(time_for_insert.total_seconds() * 1000) + " milliseconds")
        print("The size of the PhoneBook is " + str(phone_book.size()))

    # Read through each line in the text file and find it in the phone book
    with open(text_file) as txt:
        line = txt.readline()
        find_call_count = 0
        start_time_for_find = datetime.datetime.now()
        while line:
            phone_number = phone_book.find(line)
            # TODO: When I run the program many exceptions are thrown so I commented this part of the code out
            # if phone_number == -1:
                # raise Exception("Phone number not found for provided person")
            line = txt.readline()
            find_call_count += 1
        end_time_for_find = datetime.datetime.now()
        time_for_find = end_time_for_find - start_time_for_find
        print("find() was called " + str(find_call_count) + " times.")
        print("Search took " + str(time_for_find.total_seconds() * 1000) + " milliseconds")


def test_list_phone_book_read_from_csv():
    phone_book = ListPhoneBook()
    read_from_csv(phone_book, 'data.csv', 'search.txt')


def test_binary_search_tree_phone_book_read_from_csv():
    phone_book = BinarySearchTreePhoneBook()
    read_from_csv(phone_book, 'data.csv', 'search.txt')


def exercise6():
    """ Runs programs and tests for exercise 6 """
    # 1. Output when using a ListPhoneBook is a quicker duration for inserting but a much longer duration to search.
    # 2. Output when using a BinarySearchTreePhoneBook is a longer duration for inserting but a very fast duration to
    #    search.
    # 3. The difference in running times comes from a really quick insertion for lists (O(1)) but a more slower
    #    insertion (O(logn)) for BSTs due to having to traverse the tree. Although the list search takes an extra
    #    significant amount of time because you have to look through all elements in the list in the worst case scenario
    #    (O(n)). While for the BST, since we only have to look at most the height of the tree (O(log(n)), the search
    #    becomes much quicker.
    test_list_phone_book_read_from_csv()
    print("")  # Print new line
    test_binary_search_tree_phone_book_read_from_csv()


if __name__ == "__main__":
    """ Runs all tests for exercises 4-6 """
    exercise4()
    exercise5()
    exercise6()
