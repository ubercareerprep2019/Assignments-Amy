# Part 3-4: Graphs (Exercise 1-4)

from common import Queue


# Exercise 1: Implement a graph using adjacency list
class GraphNode(object):
    def __init__(self, data: int):
        self.data = data


class GraphWithAdjacencyList(object):
    def __init__(self):
        self.adjNodes = {}

    def addNode(self, key: int):
        """ Adds a new node to the graph """
        if key not in self.adjNodes:
            node_to_insert = GraphNode(key)
            self.adjNodes[node_to_insert] = []

    def removeNode(self, key: int):
        """ Removes the node from the graph """
        # Delete actual node
        node_to_remove = self.getNode(key)
        del self.adjNodes[node_to_remove]

        # Look through rest of adjacency list and remove references
        val_list = self.adjNodes.values()
        for curr_val_list in val_list:
            if node_to_remove in curr_val_list:
                curr_val_list.remove(node_to_remove)

    def addEdge(self, node1: int, node2: int):
        """ Adds an edge between node 1 and node 2 """
        nodes = self.getAdjNodes(node1)
        node_2 = self.getNode(node2)
        if node_2 not in nodes:
            nodes.append(node_2)

    def removeEdge(self, node1: int, node2: int):
        """ Removes an edge between node 1 and node 2 """
        nodes = self.getAdjNodes(node1)
        node_2 = self.getNode(node2)
        if node_2 in nodes:
            nodes.remove(node_2)

    def getAdjNodes(self, key: int):
        return self.adjNodes[self.getNode(key)]

    # Helper Functions
    def getNode(self, key: int):
        # Note: I had a hard time figuring how to get the same node without searching for it every time since I only had
        # an int to represent the key. Although I know this isn't the most efficient solution.
        for key_node in self.adjNodes.keys():
            if key_node.data == key:
                return key_node

    # Exercise 2: DFS Traversal
    def DFS(self, key: int):
        """ Starts at an arbitrary root node and explores nodes as deeper as possible along each branch  """
        self.dfs_helper(key, [])

    def dfs_helper(self, key, visted_nodes):
        root_node = self.getNode(key)
        print(root_node.data)
        visted_nodes.append(root_node)

        children = self.getAdjNodes(root_node.data)
        if not children:
            return
        else:
            for child in children:
                if child not in visted_nodes:
                    child_val = child.data
                    visted_nodes.append(child_val)
                    self.dfs_helper(child_val, visted_nodes)

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

    # Exercise 3: BFS Traversal
    def BFS(self, key: int):
        """ Starts at an arbitrary root node and explores all neighboring node at same level """
        nodes_to_print = Queue()
        nodes_to_print.enqueue(self.getNode(key))

        visited_nodes = []  # Keep track of nodes printed in order to not print the same node twice

        while not nodes_to_print.isEmpty():  # Dequeue node
            curr_node = nodes_to_print.dequeue()
            if curr_node is not None:
                if curr_node not in visited_nodes:  # Don't enqueue nodes we have seen
                    print(curr_node.data)
                    visited_nodes.append(curr_node)

                    children = self.getAdjNodes(curr_node.data)
                    if children:
                        for child in children:
                            if child not in visited_nodes:
                                nodes_to_print.enqueue(child)

    # Exercise 4: Minimum number of edges between two nodes of a Graph
    def minNumberOfEdges(self, node1: int, node2: int):
        """ Starts at an arbitrary root node and explores all neighboring node at same level """
        nodes_to_check = Queue()
        nodes_to_check.enqueue(self.getNode(node1))

        visited_nodes = []
        distances_from_node1 = {}  # Use a map to keep track of which node we are referring to

        while not nodes_to_check.isEmpty():  # Dequeue node
            curr_node = nodes_to_check.dequeue()
            if curr_node is not None:
                if curr_node not in visited_nodes:  # Don't enqueue nodes we have seen
                    # print(curr_node.data)
                    visited_nodes.append(curr_node)
                    # Had a difficult time thinking about this one. I know we have to somehow recursively look through
                    # the nodes and find the distance from node 1 to all other nodes. By looking at all other nodes we
                    # can update the shortest number of edges and then return the distance within distances_from_node1
                    # for node 2. I initially thought that maybe BFS would be useful but I am having a hard time
                    # thinking about how do we know which intermediate nodes connect to node 2.


# Tests for exercise 1
def test_add_node():
    graph = GraphWithAdjacencyList()
    graph.addNode(3)
    assert(len(graph.adjNodes) == 1)
    all_nodes = list(graph.adjNodes.keys())
    assert(all_nodes[0].data == 3)


def test_remove_node():
    graph = GraphWithAdjacencyList()
    graph.addNode(3)
    graph.removeNode(3)
    assert(len(graph.adjNodes) == 0)


def test_add_edge():
    graph = GraphWithAdjacencyList()
    graph.addNode(5)
    graph.addNode(3)
    graph.addEdge(5, 3)
    assert(graph.adjNodes[graph.getNode(5)] == [graph.getNode(3)])


def test_remove_edge():
    graph = GraphWithAdjacencyList()
    graph.addNode(5)
    graph.addNode(3)
    graph.addEdge(5, 3)
    graph.removeEdge(5, 3)
    assert(graph.adjNodes[graph.getNode(5)] == [])


def test_get_adj_nodes():
    graph = GraphWithAdjacencyList()
    graph.addNode(3)
    graph.addNode(5)
    graph.addNode(7)
    graph.addEdge(3, 5)
    graph.addEdge(3, 7)
    assert(graph.adjNodes[graph.getNode(3)] == graph.getAdjNodes(3))


def test_exercise_1():
    """ Runs all tests for exercise 1 """
    test_add_node()
    test_remove_node()
    test_add_edge()
    test_remove_edge()
    test_get_adj_nodes()


# Exercise 2: DFS Traversal
# Note: Implementation is above within the GraphWithAdjacencyList class definition

# Tests for exercise 2
def sample_graph():
    graph = GraphWithAdjacencyList()
    graph.addNode(2)
    graph.addNode(0)
    graph.addNode(1)
    graph.addNode(3)
    graph.addEdge(0, 2)
    graph.addEdge(0, 1)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(2, 1)
    graph.addEdge(3, 3)
    return graph


def test_DFS():
    print("Printing the output of the DFS call ...")
    graph = sample_graph()
    graph.DFS(2)


def test_exercise_2():
    """ Runs all tests for exercise 2 """
    test_DFS()


# Exercise 3: BFS Traversal
# Note: Implementation is above within the GraphWithAdjacencyList class definition

# Tests for exercise 3
def test_BFS():
    print("Printing the output of the BFS call ...")
    graph = sample_graph()
    graph.BFS(2)


def test_exercise_3():
    """ Runs all tests for exercise 3 """
    test_BFS()


# Exercise 4: Minimum number of edges between two nodes of a Graph
# Note: Implementation is above within the GraphWithAdjacencyList class definition

# Tests for exercise 4
def sample_graph_edges():
    graph = GraphWithAdjacencyList()
    graph.addNode(0)
    graph.addNode(1)
    graph.addNode(2)
    graph.addNode(3)
    graph.addNode(4)
    graph.addNode(5)
    graph.addNode(6)
    graph.addEdge(0, 1)
    graph.addEdge(1, 0)
    graph.addEdge(0, 2)
    graph.addEdge(2, 0)
    graph.addEdge(0, 4)
    graph.addEdge(4, 0)
    graph.addEdge(1, 2)
    graph.addEdge(2, 5)
    graph.addEdge(5, 2)
    graph.addEdge(3, 4)
    graph.addEdge(4, 3)
    graph.addEdge(4, 5)
    graph.addEdge(5, 4)
    graph.addEdge(4, 6)
    graph.addEdge(6, 4)
    return graph

def test_exercise_4():
    """ Runs all tests for exercise 4 """
    graph = sample_graph_edges()
    # assert(graph.minNumberOfEdges(1, 5) == 2)
    # assert(graph.minNumberOfEdges(6, 1) == 3)


if __name__ == "__main__":
    """ Runs all tests for exercises 1 - 3 """
    test_exercise_1()
    test_exercise_2()
    test_exercise_3()
    test_exercise_4()
