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
        
def dijkstra(graph, start, distances={}, visited={}, candidates=[]):
    visited[start] = 1
    distances[start] = 0
    for neighbor in graph[start]:
        heapq.heappush(candidates, neighbor)
    while candidates != []:
        exploredVertex = heapq.heappop(candidates)
        if exploredVertex[1] not in visited:
            visited[exploredVertex[1]] = 1
            distances[exploredVertex[1]] = exploredVertex[0]
            for neighbor in graph[exploredVertex[1]]:
                if neighbor[1] not in visited:
                    candidateDistance = exploredVertex[0] + neighbor[0]
                    candidate = [candidateDistance, neighbor[1]]
                    heapq.heappush(candidates, candidate)
    return distances

distances = dijkstra(x, 0)
for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
    print(distances[i-1])
