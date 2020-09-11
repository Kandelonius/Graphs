# from graph.graph import Graph

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # create an empty set to hold the vertices
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if the vertices exist and add them if they do.
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1) automatically bidirectional, undirected
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    """
    given a node(starting_node), return the furthest ancestor node.
    If no parents exist return -1
    The input will not be empty
    there are no cycles
    there are no repeated nodes
    IDs will always be positive
    a parent may have any number of children
    """
    graph = Graph()
    for relationship in ancestors:
        # print(relationship[0])
        graph.add_vertex(relationship[0])
        graph.add_vertex(relationship[1])
    for relationship in ancestors:
        graph.add_edge(relationship[1], relationship[0])
    # print(graph)
    # take in starting node and do dfs returning the longest result?
    # create stack to hold nodes to check
    check = Queue()
    # add starting_node to the stack
    check.enqueue([starting_node])
    # create a set to hold visited nodes
    visited = set()
    print(f"check.size is {check.size()}")
    # set up while loop to traverse until the stack is empty checking for the value
    oldest_ancestor = []
    # oldest_ancestor = set()
    while check.size() > 0:
        print(f"check.size inside is {check.size()}")
        # add the current item to path
        # print(graph)
        path = check.dequeue()
        current = path[-1]
        if current not in visited:
            visited.add(current)
        # print(f"current is {current} and neighbor {graph.get_neighbors(current)}")
        for neighbor in graph.get_neighbors(current):
            # copy the path so far to be forked as necessary
            fork = list(path)
            fork.append(neighbor)
            check.enqueue(fork)
            print(f"fork is {fork}")

            oldest_ancestor.append(fork[-1])
            print(oldest_ancestor)
            # if neighbor == None:
            #     # print("hello")
            # else:
            #     # print("why did we stop running?")
            #     temp = path[:]
            #     temp.append(neighbor)
            #     check.enqueue(temp)
        if oldest_ancestor == []:
            return -1
    return oldest_ancestor[-1]