'''
Graph data structure
- dictionary of node : list(node), where a node in the list represents an edge
- method addEdge adds an edge between two dictionarys
'''

from collections import defaultdict

class DirectedGraph:

    def __init__(self):
        self._graph = defaultdict(list)
        self._count = 0

    def size(self):
        return self._count

    def addEdge(self, u, v):
        self._graph[u].append(v)
        if max(u, v) + 1 > self._count:
            self._count = max(u, v) + 1

    def nodes(self):
        return self._graph.keys()

    def edges(self, s):
        return self._graph[s]

    def __str__(self):
        return(str(self._graph))

class UndirectedGraph(DirectedGraph):
    def addEdge(self, u, v):
        self._graph[u].append(v)
        self._graph[v].append(u)
        if max(u, v) + 1 > self._count:
            self._count = max(u, v) + 1