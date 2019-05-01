#This is the fourth coding assignment for Algorithms I from Stanford Lagunita
#The task is to implement kosaraju's algorithm
#for computing the strongly-connected components of a directed graph
#and report the length of the largest 5 in the provided graph

import sys
sys.setrecursionlimit(1000)

graph = []
inverseGraph = []
with open("SCC.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        outVertex = int(splitline[0])-1
        inVertex = int(splitline[1])-1
        while outVertex >= len(graph):
            graph.append([])
        graph[outVertex].append(inVertex)
        while inVertex >= len(inverseGraph):
            inverseGraph.append([])
        inverseGraph[inVertex].append(outVertex)

def traverse(graph, L):
    for node in range(len(graph)):
        if node not in L:
            L = visit(graph, L, node)
    L.reverse()
    return L

def visit(graph, L, node):
    L.append(node)
    for neighbor in graph[node]:
        if neighbor not in L:
            L = visit(graph, L, neighbor)
    L.remove(node)
    L.append(node)
    return L

def assignRoots(invGraph, L, R):
    for node in L:
        R = assign(invGraph, R, node, node)
    return R
        
def assign(invGraph, R, node, root):
    if R[node] == []:
        R[node] = root
        for neighbor in invGraph[node]:
            R = assign(invGraph, R, neighbor, root)
    return R

# graph = [[1],[2],[3, 4],[1],[5],[4]]
# invGraph = [[], [3], [1], [2], [2,5], [4]]
        
L = []
R = []
for i in range(len(inverseGraph)):
    R.append([])
    
L = traverse(graph, L)
R = assignRoots(inverseGraph, L, R)


Components = [0]*len(R)
for node in R:
    Components[node] += 1
print(sorted(Components, reverse=True)[:5])
