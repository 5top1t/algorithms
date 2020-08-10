'''
Starting at the root node, explore every edge that leads
to an unvisited node. Queue the nodes to be visited in the
order they are discorved and repeat this process on each node
until the queue is empty.

For each of those edges explore the graph

runtime: O(E+V)
space complexity: O(V)
'''

def bfs(g, s): 
    n = len(g.nodes())
    visited = [False] * g.size()
    queue = [s]
    visited[s] = True

    while queue:

        s = queue.pop(0)
        print(s)
        
        for e in g.edges(s):
            if not visited[e]:
                queue.append(e)
                visited[e] = True


from graph import DirectedGraph

g = DirectedGraph()
g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 3)
g.addEdge(3, 3)
g.addEdge(3, 4)
g.addEdge(4, 2)
print(g)

bfs(g, 0)











