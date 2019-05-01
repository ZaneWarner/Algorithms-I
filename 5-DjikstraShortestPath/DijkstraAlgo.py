#This is the fifth coding assignment for Algorithms I from Stanford Lagunita
#The task is to implement dijkstra's algorithm
#To compute the shortest-path distances for the vertices of a given graph
#And report ten particular shortest-path distances
#I will be taking the optional step of using a heap-based implementation for improved performance

import heapq

x = []
#This represents the graph as an adjacency list, where [edge length, neighbor] pairs are listed for each edge
with open("dijkstraData.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        edgelist = []
        for num in splitline[1:]:
            edge = num.split(',')
            edge[0], edge[1] = int(edge[1]), int(edge[0])-1
            edgelist.append(edge)
        x.append(edgelist)
        
def dijkstra(graph, start):
    distances, visited, candidates = {}, set(), [] 
    visited.add(start)
    distances[start] = 0
    for neighbor in graph[start]:
        heapq.heappush(candidates, neighbor) #candidates becomes a heap to track which node is best to explore next
    while candidates != []:
        explored = heapq.heappop(candidates)
        node, distance = explored[1], explored[0]
        if node not in visited:
            visited.add(node)
            distances[node] = distance
            for neighbor in graph[node]:
                if neighbor[1] not in visited:
                    candidateDistance = distance + neighbor[0]
                    candidate = [candidateDistance, neighbor[1]]
                    heapq.heappush(candidates, candidate)
    return distances

distances = dijkstra(x, 0)
for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
    print(distances[i-1])
