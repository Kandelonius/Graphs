"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # bft uses queue dft uses stack
        # use built-in empty queue
        q = Queue()

        # add starting vertex to the queue
        q.enqueue(starting_vertex)

        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue vertex
            v = q.dequeue()

            # if we haven't visited it
            if v not in visited:
                # print
                print(v)
                # mark as visited
                visited.add(v)
                # add all neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # bft uses queue dft uses stack
        # use built-in empty queue
        s = Stack()

        # add starting vertex to the queue
        s.push(starting_vertex)

        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while s.size() > 0:
            # dequeue vertex
            v = s.pop()

            # if we haven't visited it
            if v not in visited:
                print(v)
                visited.add(v)
                # add all neighbors
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # similar to iterative solution create a set but this time add a
        # conditional to check if this is the first time through.
        if visited == None:
            visited = set()
        # add first vertex to the set
        visited.add(starting_vertex)
        # print whatever is sent as starting_vertex *initially the starting value
        print(starting_vertex)
        # checking if neighbor vertices have been visited
        # if not visit them and recursively call dft again
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        # Create a Set to store visited vertices
        visited = set()
        q.enqueue([starting_vertex])
        # While the queue is not empty...
        # print("not in loop")
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # print(f"in loop {path} destination is {destination_vertex}")
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
            current = path[-1]  # setting the newly added node to a variable
            if current not in visited:
                # print(f"current is {current} in visited loop")
                # CHECK IF IT'S THE TARGET
                if current == destination_vertex:
                    # print("surely we're not returning")
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(current)
                # print(visited)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(current):
                    # COPY THE PATH
                    # APPEND THE NEIGHBOR TO THE BACK
                    temp = path[:]
                    # print(f"neighbor is {neighbor} temp is {temp}")
                    temp.append(neighbor)
                    q.enqueue(temp)
                    # print(q)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            current = path[-1]
            if current not in visited:
                if current == destination_vertex:
                    return path
                visited.add(current)
                for neighbor in self.get_neighbors(current):
                    temp = path[:]
                    temp.append(neighbor)
                    s.push(temp)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
