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



if __name__ == '__main__':
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
