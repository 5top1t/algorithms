'''
Starting at the root node explore follow
edges untill they lead no were and recursive
return an edge to follow. Repeat this process until all the nodes are visited

runtime: O(E+V)
space complexity: O(V)
'''

def dfs(g, s):
    n = g.size()
    visited = [False] * n
    dfs_helper(g, s, visited)

def dfs_helper(g, s, visited):
    
    visited[s] = True
    print(s)

    for e in g.edges(s):
        if not visited[e]:
            dfs_helper(g, e, visited)

from graph import DirectedGraph

g = DirectedGraph()
g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 3)
g.addEdge(3, 3)
g.addEdge(3, 4)
g.addEdge(4, 2)
print(g)

dfs(g, 0)
