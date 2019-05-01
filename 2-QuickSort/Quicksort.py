#This is the second coding assignment for Algorithms I from Stanford Lagunita
#The task is to implement quicksort using three different pivot selection schemes
#With the partition subroutine implemented as specified in the lecture
#And count the number of comparisons made for each choice of pivot
#when sorting a provided list of numbers
x = []
with open("QuickSort.txt", 'r') as file:
    for line in file:
        x.append(int(line))

#pivotRule can be "low", "high", or "median"
#the first two correspond to always using the lowest and highest index, respectively
#while the third compares those with the middle-indexed element (rounded down) and uses the median
def quicksort(x, pivotRule="low"):
    if len(x) <= 1:
        return x, 0
    pivotIndex = choosePivot(x, pivotRule)
    x, pivotIndex = partition(x, pivotIndex)
    partition_comparisons = len(x)-1
    x_left, left_comparisons = quicksort(x[:pivotIndex], pivotRule) 
    x_right, right_comparisons = quicksort(x[pivotIndex+1:], pivotRule)
    x = x_left + [x[pivotIndex]] + x_right
    comparisons = partition_comparisons + left_comparisons + right_comparisons
    return x, comparisons

def choosePivot(x, pivotRule):
    xhigh = len(x)-1
    if pivotRule == "low":
        pivotIndex = 0
    elif pivotRule == "high":
        pivotIndex = xhigh
    elif pivotRule == "median":
        p_low, p_med, p_high = x[0], x[xhigh//2], x[xhigh]
        if p_low <= p_med <= p_high or p_high <= p_med <= p_low:
            pivotIndex = xhigh//2
        elif p_med <= p_low <= p_high or p_high <= p_low <= p_med:
            pivotIndex = 0
        else:
            pivotIndex = xhigh
    else: print("invalid specification of pivot rule")
    return pivotIndex
        
def partition(x, pivotIndex):
    pivot = x[pivotIndex]
    x[0], x[pivotIndex] = x[pivotIndex], x[0] #Redundant for minimum elmt pivot
    i = 1
    for j in range(len(x)):
        if x[j]<pivot:
            x[i], x[j] = x[j], x[i]
            i += 1
    x[0], x[i-1] = x[i-1], x[0]
    return x, i-1
        
x, c = quicksort(x, "median")
print(x)
print(c)