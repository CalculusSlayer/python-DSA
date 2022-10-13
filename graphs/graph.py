class Graph:
    def __init__(self, v):
        self.vertices = v
        self.edges = {i: [] for i in range(v)}

    def __repr__(self):
        return f"adjacency list representation: {self.edges}"

    def add_edge(self, u, v):
        if v not in self.edges[u]:
            early_break = False
            for i in range(len(self.edges[u])):
                if v < self.edges[u][i]:
                    self.edges[u].insert(i, v)
                    early_break = True
                    break
            if not early_break:
                self.edges[u].append(v)

        if u not in self.edges[v]:
            early_break = False
            for i in range(len(self.edges[v])):
                if u < self.edges[v][i]:
                    self.edges[v].insert(i, u)
                    break
            if not early_break:
                self.edges[v].append(u)

    def add_arc(self, u, v):
        if v not in self.edges[u]:
            early_break = False
            for i in range(len(self.edges[u])):
                if v < self.edges[u][i]:
                    self.edges[u].insert(i, v)
                    early_break = True
                    break
            if not early_break:
                self.edges[u].append(v)


def bfs(G, source):
    '''
    G: Graph object
    source: value of starting node
    '''
    if source not in G.edges.keys():
        print("Starting value not in graph")
        return

    queue = []
    queue.append(source)
    visited = set()
    visited.add(source)
    print("BFS: ", end="")
    while queue:
        x = queue.pop(0)
        print(x, end=" ")
        for neighbor in G.edges[x]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

def dfs(G, source):
    '''
    G: Graph object
    source: value of starting node
    '''

    if source not in G.edges.keys():
        print("Starting value not in graph")
        return
    stack = []
    stack.append(source)
    visited = set()
    visited.add(source)
    print("DFS: ", end="")
    while stack:
        x = stack.pop()
        print(x, end=" ")
        for neighbor in G.edges[x]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    print()


def main():
    # For BFS traversal problem 2
    g1 = Graph(10)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(0, 3)
    g1.add_edge(1, 4)
    g1.add_edge(1, 5)
    g1.add_edge(1, 6)
    g1.add_edge(3, 7)
    g1.add_edge(3, 8)
    g1.add_edge(4, 9)

    print(g1)
    bfs(g1, 0)
    print()

    # For DFS traversal problem 3
    g2 = Graph(7)
    g2.add_edge(0, 2)
    g2.add_edge(0, 1)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)
    g2.add_edge(1, 4)
    g2.add_edge(3, 5)
    g2.add_edge(4, 6)
    g2.add_edge(5, 6)
    print(g2)
    dfs(g2, 0)
    print()
    

if __name__ == "__main__":
    main()
