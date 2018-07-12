"""
Graph data structure
"""


class Node:
    """
    Node class
    """
    def __init__(self, data):
        self._data = data
        self._connections = set()
        self._visited = False
        self._nr_of_connections = 0

    def add_connection(self, to_node):
        self._connections.add(to_node)
        self._nr_of_connections += 1

    def get_connections(self):
        for connection in self._connections:
            yield connection

    def visited(self):
        return self._visited

    def visit(self):
        print(self._data)
        self._visited = True

    def eq(self, node):
        """
        Check if two nodes are equals
        """
        return node._data == self._data

    def is_leaf(self):
        """
        A leaf node is a node with no connections originated from it to other nodes
        """
        return True if self._nr_of_connections == 0 else False


class Edge:
    """
    Edge class
    """
    def __init__(self, from_, to):
        self._from = from_
        self._to = to


class Graph:
    """
    Graph structure
    """
    def __init__(self):
        self._nodes = set()
        self._edges = []
        self._cache = {}

    def add_edge(self, from_node, to_node):
        """
        Adds an edge
        """
        self._edges.append(Edge(from_node, to_node))
        from_node.add_connection(to_node)

    def create_from_dict(self, data):
        """
        Creates a graph from dictionary
        """
        for key, value in data.iteritems():
            if key not in self._cache:
                from_node = Node(key)
                self._cache[key] = from_node
                self._nodes.add(from_node)
            else:
                from_node = self._cache[key]
            for item in value:
                if item not in self._cache:
                    to_node = Node(item)
                    self._cache[item] = to_node
                    self._nodes.add(to_node)
                else:
                    to_node = self._cache[item]

                self.add_edge(from_node, to_node)

    def traverse_df(self):
        # import pdb; pdb.set_trace()
        for node in self._nodes:
            if not node.visited():
                self._traverse_df(node)

    def _traverse_df(self, node):
         node.visit()
         for connection in node.get_connections():
             if not connection.visited():
                 self._traverse_df(connection)

    def is_connection(self, from_node, to_node):
        """
        Check if there is a path between two nodes
        """
        return self._is_connection(from_node, to_node, None)


    def _is_connection(self, from_node, to_node, path):
        # import pdb; pdb.set_trace()
        if path is None:
            path = [from_node]

        if from_node.is_leaf() and from_node.eq(to_node):
            path.append(to_node)
            return path
        for node in from_node.get_connections():
            if to_node.eq(path[-1]):
                return path
            path.append(node)
            if to_node.eq(node):
                return path
            else:
                self._is_connection(node, to_node, path)
        if not to_node.eq(path[-1]):
            path.pop()
        return path



# graph strcture using adjacency matrix
import abc
import numpy as np

class AbstractGraph(abc.ABCMeta):
    """
    Abstract class to represent the interfact of the graph class
    """
    def __init__(self, num_vertices, directed=False):
        """
        Initialize new graph
        """
        self.num_vertices = num_vertices
        self.directed = directed


    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        """
        Adds new edge to the graph
        """
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        """
        Retrieves the adjacent verticies to a vertix
        """
        pass


    @abc.abstractmethod
    def get_indegree(self, v):
        """
        Retrieves the indegree of a vertix
        """
        pass


    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        """
        Gets the weight of the edge between two vertices
        """
        pass


    @abc.abstractmethod
    def display(self):
        """
        Prints the content of the graph
        """
        pass


class AdjacencyNode:
    """
    Represent a node in an Adjacent Graph
    """
    def __init__(self, vertix_idx):
        self._vertix_idx = vertix_idx
        self._connections = set()

    def add_connection(self, v):
        if v == self._vertix_idx:
            raise ValueError('Cannot add the same node as a connection to itself')
        self._connections.add(v)

    def get_adjacent_vertices(self):
        return sorted(self._connections)


class AdjacencySetGraph:
    """
    Adjacency Set representation of the a graph
    """
    def __init__(self, num_vertices, directed=False):
        """
        Initializes new graph
        """
        # super(AdjacencyMatrixGraph, self).__init__(num_vertices=num_vertices, directeed=directed)
        self.num_vertices = num_vertices
        self.directed = directed
        self.nodes = []
        for i in range(num_vertices):
            self.nodes.append(AdjacencyNode(i))


    def add_edge(self, v1, v2, weight=1):
        """
        Adds new edge to the graph
        """
        if any([v1 >= self.num_vertices, v2 >= self.num_vertices, v1 < 0, v2 < 0]):
            raise ValueError("Invalid vertix specified. Both vertices must be between {} and {}".format(0, self.num_vertices -1))

        if weight != 1:
            raise ValueError("Invalid value for the weight of an edge. Edge wieght must be 1")

        self.nodes[v1].add_connection(v2)

        if self.directed is False:
            self.nodes[v2].add_connection(v1)


    def get_adjacent_vertices(self, v):
        """
        Retrieves the adjacent verticies to a vertix
        """
        if any([v < 0, v >= self.num_vertices]):
            raise ValueError("Invalid vertix specified. Both vertices must be between {} and {}".format(0, self.num_vertices -1))
        return self.nodes[v].get_adjacent_vertices()

    def get_indegree(self, v):
        """
        Retrieves the indegree of a vertix
        """
        if any([v < 0, v >= self.num_vertices]):
            raise ValueError("Invalid vertix specified. Both vertices must be between {} and {}".format(0, self.num_vertices -1))
        result = 0
        for node in self.nodes:
            if v in node.get_adjacent_vertices():
                result += 1
        return result


    def get_edge_weight(self, v1, v2):
        """
        Gets the weight of the edge between two vertices
        """
        return 1


    def display(self):
        """
        Prints the content of the graph
        """
        for i in range(self.num_vertices):
            for v in self.nodes[i].get_adjacent_vertices():
                print(i, "-->", v)


class AdjacencyMatrixGraph:
    """
    Adjacency Matrix representation of a graph
    """
    def __init__(self, num_vertices, directed=False):
        """
        Initializes new graph
        """
        # super(AdjacencyMatrixGraph, self).__init__(num_vertices=num_vertices, directeed=directed)
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = np.zeros((num_vertices, num_vertices))


    def add_edge(self, v1, v2, weight=1):
        """
        Adds new edge to the graph
        """
        if any([v1 >= self.num_vertices, v2 >= self.num_vertices, v1 < 0, v2 < 0]):
            raise ValueError("Invalid vertix specified. Both vertices must be between {} and {}".format(0, self.num_vertices -1))

        if weight < 1:
            raise ValueError("Invalid value for the weight of an edge. Edge wieght must be >= 1")

        self.matrix[v1][v2] = weight

        if self.directed is False:
            self.matrix[v2][v1] = weight


    def get_adjacent_vertices(self, v):
        """
        Retrieves the adjacent verticies to a vertix
        """
        if any([v < 0, v >= self.num_vertices]):
            raise ValueError("Invalid vertix specified. Both vertices must be between {} and {}".format(0, self.num_vertices -1))
        result = []
        for vertix in range(self.num_vertices):
            if self.matrix[v][vertix] > 0:
                result.append(vertix)
        return result

    def get_indegree(self, v):
        """
        Retrieves the indegree of a vertix
        """
        if any([v < 0, v >= self.num_vertices]):
            raise ValueError("Invalid vertix specified. Both vertices must be between {} and {}".format(0, self.num_vertices -1))
        result = 0
        for vertix in range(self.num_vertices):
            if self.matrix[vertix][v] > 0:
                result += 1
        return result


    def get_edge_weight(self, v1, v2):
        """
        Gets the weight of the edge between two vertices
        """
        if any([v1 >= self.num_vertices, v2 >= self.num_vertices, v1 < 0, v2 < 0]):
            raise ValueError("Invalid vertix specified. Both vertices must be between {} and {}".format(0, self.num_vertices -1))
        return self.matrix[v1][v2]


    def display(self):
        """
        Prints the content of the graph
        """
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(v=i):
                print(i, "-->", v)


def test_AdjacentGraph(adj_set=False):
    if adj_set:
        g = AdjacencySetGraph(4)
    else:
        g = AdjacencyMatrixGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)

    for i in range(4):
        print("Adjacents to: ", i, " are: ", g.get_adjacent_vertices(i))

    for i in range(4):
        print("Indegree of: ", i, " is: ", g.get_indegree(i))

    for i in range(4):
        for j in g.get_adjacent_vertices(i):
            print("Edge between ", i, " --> ", j, " has weight: ", g.get_edge_weight(i, j))

    g.display()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'adjacent':
        test_AdjacentGraph(True)
    else:
        # data = {0: [1], 1: [2], 2: [0, 3], 3: [2], 4: [6], 5: [4], 6: [5]}
        data = {2: [], 1: [3, 5], 3: [11], 11: [20], 20: [], 5: [30, 7], 7: [3, 30], 30: []}
        # data = {1: [3, 2, 4], 3: [5], 2: [7], 4: [], 7: [], 5: []}
        graph = Graph()
        graph.create_from_dict(data)
        graph.traverse_df()
        from_node = [node for node in graph._nodes if node._data == 1][0]
        to_node = [node for node in graph._nodes if node._data == 20][0]
        path = graph.is_connection(from_node, to_node)
        if path:
            print('->'.join([str(node._data) for node in path]))
        else:
            print('No path')
