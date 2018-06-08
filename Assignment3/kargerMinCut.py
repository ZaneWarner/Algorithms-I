#This is the third coding assignment for Algorithms I from Stanford Lagunita
#The task is to implement the karger randomized contraction algorithm
#to compute the minimum cut from an adjacency list representation of an undirected graph
import random
import copy

x = []
with open("kargerMinCut.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        linelist =[]
        for num in splitline[1:]:
            linelist.append(int(num))
        x.append(linelist)

def kargerRandomContraction(x):
    while len(x) > 2:
        vert1, vert2 = selectRandomEdge(x)
        x = contractEdge(x, vert1, vert2)
    return len(x[0])
    

def contractEdge(x, vert1, vert2):
    while vert2 in x[vert1-1]:
        x[vert1-1].remove(vert2)
    for edge in x[vert2-1]:
        if edge != vert1:
            x[vert1-1].append(edge)
    del x[vert2-1]
    for row in range(len(x)):
        for edge in range(len(x[row])):
            if x[row][edge] == vert2:
                x[row][edge] = vert1
            if x[row][edge] > vert2:
                x[row][edge] -= 1
    return x
        
def selectRandomEdge(x):
    flat_x = [num for sublist in x for num in sublist]
    edge_num = random.randint(1, len(flat_x))
    count, row = 0, 0
    while count < edge_num:
        if count+len(x[row]) < edge_num:
            count += len(x[row])
            row += 1
        else:
            for edge in x[row]:
                count += 1
                if count == edge_num:
                    return row+1, edge

minCuts = []
for i in range(15):
    graph = copy.deepcopy(x)
    minCut = kargerRandomContraction(graph)
    minCuts.append(minCut)
print(minCuts)
print(min(minCuts))
    