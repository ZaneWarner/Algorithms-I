#This is the first coding assignment for Algorithms I from Stanford Lagunita
#The task is, given an array of numbers, to count the inversions in nlogn time
#This is accomplished by implementing mergesort, 
#and counting how often a number is merged from the right-side array

x = []
with open("IntegerArray.txt", 'r') as file:
    for line in file:
        x.append(int(line))

def sortAndCount(x):
    if len(x) <= 1:
        return x, 0
    midpoint = len(x)//2
    left_x = x[:midpoint]
    right_x = x[midpoint:]
    sorted_left, left_inversions = sortAndCount(left_x)
    sorted_right, right_inversions = sortAndCount(right_x)
    sorted_x, split_inversions = merge(sorted_left, sorted_right)
    return sorted_x, left_inversions+right_inversions+split_inversions

def merge(left_x, right_x):
    sorted_x = []
    inversions = 0
    while len(left_x) > 0 and len(right_x) > 0:
        if left_x[0] <= right_x[0]:
            sorted_x.append(left_x[0])
            del left_x[0]
        else:
            sorted_x.append(right_x[0])
            inversions += len(left_x)
            del right_x[0]
    while len(left_x) > 0:
        sorted_x.append(left_x[0])
        del left_x[0]
    while len(right_x) > 0:
        sorted_x.append(right_x[0])
        del right_x[0]
    return sorted_x, inversions

s, i = sortAndCount(x)
print(i)
