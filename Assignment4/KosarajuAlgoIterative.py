#This is the fourth coding assignment for Algorithms I from Stanford Lagunita
#The task is to implement kosaraju's algorithm
#for computing the strongly-connected components of a directed graph
#and report the length of the largest 5 in the provided graph
#This is an iterative reconstruction of the recursive implementation I made,
#which ran into python's recursion limit (and caused a stack overflow if that limit was lifted)

def traverse(graph, L):
    visited = {}
    for root in range(len(graph)):
        if root not in visited:
            path = [[root]]
            visited[root] = 1
            while path != []:
                while path[-1] != []:
                    node = path[-1][0]
                    unexploredNeighbors = []
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            unexploredNeighbors.append(neighbor)
                            visited[neighbor] = 1
                    if unexploredNeighbors == []:
                        L.append(node)
                        del path[-1][0]
                    else:
                        path.append(unexploredNeighbors)
                del path[-1]
    return L

def assignRoots(invGraph, L, R):
    assigned = {}
    while L != []:
        root = L.pop()
        path = []
        if root not in assigned:
            path = [[root]]
            R[root] = root
            assigned[root] = 1
        while path != []:
                while path[-1] != []:
                    node = path[-1][0]
                    R[node] = root
                    assigned[node] = 1
                    unexploredNeighbors = []
                    for neighbor in invGraph[node]:
                        if neighbor not in assigned:
                            unexploredNeighbors.append(neighbor)
                    del path[-1][0]
                    if unexploredNeighbors != []:
                        path.append(unexploredNeighbors)
                del path[-1]
    return R
        

# graph = [[1],[1,2,3],[0],[4],[3],[0,7],[5],[6]]
# inverseGraph = [[5,2],[0,1],[1],[1,4],[3],[6],[7],[5]]
#   
# L = traverse(graph, [])
# print(L)
# R = assignRoots(inverseGraph, L, {})
# print(R)
# ClusterLens = [0]*len(R)
# for key in R:
#     ClusterLens[R[key]] += 1
# print(sorted(ClusterLens, reverse=True)[:5])
graph = []
with open("SCC.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        outVertex = int(splitline[0])-1
        inVertex = int(splitline[1])-1
        while inVertex >= len(graph) or outVertex >= len(graph):
            graph.append([])
        graph[inVertex].append(outVertex)
    
print("traversing graph")
L = traverse(graph, [])
print("graph traversed, L has len {}".format(len(L)))
del graph
   
invGraph = []
with open("SCC.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        outVertex = int(splitline[0])-1
        inVertex = int(splitline[1])-1
        while outVertex >= len(invGraph):
            invGraph.append([])
        invGraph[outVertex].append(inVertex)

           
print("assigning roots")
R = [0]*len(invGraph) 
R = assignRoots(invGraph, L, R)
del invGraph
ClusterLens = [0]*len(R)
print("len R {}".format(len(R)))
for key in R:
    ClusterLens[R[key]] += 1
print(sorted(ClusterLens, reverse=True)[:5])

