from graph import Graph, bfs, dfs

def directedGraph_test1():
    print("Direct Graph Test 1")
    g = Graph(5)
    g.add_arc(0, 1)
    g.add_arc(1, 2)
    g.add_arc(2, 3)
    g.add_arc(3, 4)
    g.add_arc(4, 0)
    print(g)

def bfs_test1():
    g2 = Graph(12)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(0, 3)
    g2.add_edge(1, 4)
    g2.add_edge(1, 5)
    g2.add_edge(1, 6)
    g2.add_edge(3, 7)
    g2.add_edge(3, 8)
    g2.add_edge(4, 11)
    g2.add_edge(5, 9)
    g2.add_edge(7, 10)
    print(g2)
    bfs(g2, 0)

def main():
    directedGraph_test1()
#    bfs_test1()
    


if __name__ == "__main__":
    main()

