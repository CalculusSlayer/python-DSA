
# Python Program to detect cycle in an undirected graph
from collections import defaultdict
 
# This class represents a undirected
# graph using adjacency list representation
 
 
class Graph:
 
    def __init__(self, vertices):
 
        # No. of vertices
        self.V = vertices  # No. of vertices
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
    
    def __str__(self):
        return str(dict(self.graph))
 
    # Function to add an edge to graph
    def addEdge(self, v, w):
        '''
        def detect-cycle(graph):
            initialize an empty set called visited

            def helper(vertex, parent):
                
        '''
 
        # Add w to v_s list
        self.graph[v].append(w)
 
        # Add v to w_s list
        self.graph[w].append(v)
    
    def stackDetectCycle(self):
        visited = [False] * self.V
        stack = [(0, None)]
        cycleFound = False
        while len(stack) != 0 and not cycleFound:
            x, parent = stack.pop()
            if visited[x] == False:
                print(x, parent)
                visited[x] = True
                for neighbor in self.graph[x]:
                    stack.append((neighbor, x))
                    if visited[neighbor] == True and neighbor != parent:
                        cycleFound = True
                        break
        print(stack)
        if cycleFound:
            cycle_vertex = stack[-1][0]
            sol = [cycle_vertex]
            for i in range(len(sol)-2, -1, -1):
                a = stack[i][0]
                if a == cycle_vertex:
                    break
                else:
                    sol.append(stack[i][0])
            return str(sol)
        else:
            return "No cycle found"


 
    # Returns true if the graph
    # contains a cycle, else false.

    # def detectCycle(self):
    #     visited = [False] * self.V
    #     sol = []
    #     def detectCycleHelper(v, visited, parent):
    #         nonlocal sol
    #         visited[v] = True
    #         for neighbor in self.graph[v]:
    #             if visited[neighbor] == True:
    #                 if neighbor != parent:
    #                     sol.append(neighbor)
    #                     #print(sol)
    #                     return True
    #             elif detectCycleHelper(neighbor, visited, v):
    #                 sol.append(neighbor)
    #                 #print(sol)
    #                 return True
    #     detectCycleHelper(0, visited, None)
    #     if len(sol) != 0:
    #         sol.append(sol[0])
    #     return sol


 
    # def isCyclic(self): 
    #     # Mark all the vertices
    #     # as not visited
    #     visited = [False]*(self.V)
    #     sol = None

    #             # A recursive function that uses
    #     # visited[] and parent to detect
    #     # cycle in subgraph reachable from vertex v.
    #     def isCyclicUtil(v, visited, parent_arr):
    #         nonlocal sol
    #         print(f"{v}, {visited}, {parent_arr}")
    
    #         # Mark the current node as visited
    #         visited[v] = True
    
    #         # Recur for all the vertices  
    #         # adjacent to this vertex
    #         for i in self.graph[v]:
    
    #             # If the node is not
    #             # visited then recurse on it
    #             if visited[i] == False:
    #                 print("append")
    #                 parent_arr.append(v)
    #                 print(parent_arr)

    #                 if isCyclicUtil(i, visited, parent_arr):
    #                     parent_arr.pop()
    #                     print("True pop")
    #                     print(parent_arr)

    #                     return True

    #             # If an adjacent vertex is
    #             # visited and not parent
    #             # of current vertex,
    #             # then there is a cycle
    #             elif parent_arr[-1] != i:
    #                 #print(f"BUG??? {parent_arr}")
    #                 parent_arr.append(i)
    #                 sol = parent_arr[1:]
    #                 print("sol pop")
    #                 parent_arr.pop()
    #                 #print(parent_arr)
    #                 return True

    #         print("False pop")
    #         parent_arr.pop()
    #         print(parent_arr)
    #         return False
 
    #     # Call the recursive helper
    #     # function to detect cycle in different
    #     # DFS trees

    #     # THIS IS ONLY NEEDED FOR DISCONNECTED GRAPHS!

    #     # for i in range(self.V):
 
    #     #     # Don't recur for u if it
    #     #     # is already visited
    #     #     if visited[i] == False:
    #     #         if(self.isCyclicUtil
    #     #            (i, visited, -1)) == True:
    #     #             return True
 
    #     # return False

    #     # FOR CONNECTED
    #     p = [None]
    #     if isCyclicUtil(0, visited, p):
    #         print(f"There exists a cycle of {sol}")
    #     else:
    #         print("No cycle exists")
    #     p.pop()
    #     # print(f"p={p}")
    #     # print(sol)






def main():
    # Create a graph given in the above diagram
    # g = Graph(5)
    # g.addEdge(1, 0 )
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(0, 3)
    # g.addEdge(3, 4)
    # print(g)

    g2 = Graph(5)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    g2.addEdge(3, 4)
    #g2.addEdge(2, 0)
    g2.addEdge(3, 1)
    #print(g2)
    print(g2.stackDetectCycle())

    #print(g2.isCyclic())
    
    # g2.addEdge(4, 0)
    # print(g2)
    # g2.isCyclic()



if __name__ == "__main__":
    main()