#This is part 1 of the sixth and final coding assignment for Algorithms I from Stanford Lagunita
#The task is to solve a variant of the 2SUM problem
#Where, given a list of ints as input, I find how many numbers in the interval [-10000,10000]
#Can be represented as a sum of two distinct ints from that list

# There is a simple hash table-based solution that runs in linear time for a given target
# Discussed in the course
# However it does not scale well with additional targets, so instead I use a two-pointers method
# Which allows the targets to share work by pre-sorting

t_low, t_high = -10000, 10000
l = []
with open("2sum.txt", 'r') as file:
    for line in file:
        line = line.strip()
        l.append(int(line))

l.sort()

lowIndex = 0
highIndex = len(l)-1
T = {}
highSet = -1
while highIndex > lowIndex:
    l_i, l_j = l[lowIndex], l[highIndex]
    sumValue = l_i + l_j
    if sumValue < t_low:
        lowIndex += 1
        if highSet != -1:
            highIndex = highSet
            highSet = -1
    elif sumValue > t_high:
        highIndex -= 1
    else:
        if highSet == -1:
            highSet = highIndex
        if l_i != l_j:
            T[sumValue] = 1
        highIndex -= 1

countHits = 0   
for key in T:
    countHits += 1
print(countHits)
            

