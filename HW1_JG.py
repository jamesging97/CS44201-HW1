# James Gingerich  
# HW1
# 9/20/2020

from collections import defaultdict 

# Class that creates graph and then can search with BFS/DFS traversal methods.
class Search: 
    def __init__(self): 
  
        # Makes a dictionary storing type of list to store the graph.
        self.graph = defaultdict(list) 
  
    # Adds an edge.
    def newEdge(self,x,y): 
        self.graph[ord(x)].append(ord(y)) 
  
    # Prints BFS traversal.
    def BFS(self, first): 
  
        # Create list of bools to keep track of found nodes.
        found = [False] * len(self.graph)
        
        # Create list for node traversal.
        nodes = []
  
        # Mark as found, add to list to search connected nodes, and print node.
        nodes.append(first) 
        found[first - ord('A')] = True
        print (chr(first), " ") 
  
        while nodes: 
  
            # pop off last traversed node.
            node = nodes.pop(0) 
            
            # Cycle through all the connected nodes.
            for i in self.graph[node]: 
                # Checks if node is new.
                if found[i - ord('A')] == False: 
                    # Prints new node.
                    print (chr(i), " ")
                    
                    # Adds to nodes list to search the nodes connections, if any.
                    nodes.append(i) 
                    
                    # Marks new node as found.
                    found[i - ord('A')] = True
                else:
                    # Print to show full search.
                    print (chr(i), "(already found)" )
                    
    # Helper method to recursive DFS to create class member and call DFS().
    def triggerDFS(self, first_node):
        found = [False] * len(self.graph)
        print (chr(first_node), " ")
        self.DFS(first_node, found)
    
    def DFS(self, first_node, found): 
            # Same as BFS above, but simplified with recursion.
            for i in self.graph[first_node]:
                if found[i - ord('A')] == False: 
                    print (chr(i), " ")
                    found[i - ord('A')] = True
                    self.DFS(i, found)
                else:
                    print (chr(i), "(backtracking)" )
  
# Create the desired diagram.
graph = Search()
graph.newEdge('C', 'D') 
graph.newEdge('E', 'F')
graph.newEdge('E', 'D')
graph.newEdge('B', 'C') 
graph.newEdge('D', 'B') 
graph.newEdge('C', 'E') 
graph.newEdge('A', 'C')  
graph.newEdge('A', 'B')
graph.newEdge('F', 'D') 

# Print BFS/DFS traversals
print ("(BFS) Beginning at vertex A:") 
graph.BFS(ord('A')) 
print ("(DFS) Beginning at vertex A:")
graph.triggerDFS(ord('A')) 
