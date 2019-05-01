#This is part 2 of the sixth and final coding assignment for Algorithms I from Stanford Lagunita
#The task is to use a heap to maintain the median element of an incoming stream of numbers
# And report the sum of all the medians encountered this way mod 10000
import heapq 
l = []
with open("Median.txt", 'r') as file:
    for line in file:
        l.append(int(line))

lowHeap = []
heapq.heappush(lowHeap, -l[1])
highHeap = []
heapq.heappush(highHeap, l[0])
medians = [l[0], l[1]]
for num in l[2:]:
    low = -heapq.heappop(lowHeap)
    high = heapq.heappop(highHeap)
    candidates = [low, num, high]
    candidates.sort()
    heapq.heappush(lowHeap, -candidates[0])
    heapq.heappush(highHeap, candidates[2])
    if len(lowHeap) <= len(highHeap):
        heapq.heappush(lowHeap, -candidates[1])
    else:
        heapq.heappush(highHeap, candidates[1])
    medians.append(-lowHeap[0])
print(sum(medians)%10000)
