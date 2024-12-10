'''
an array is safe, if they are either all increasing or decreasing
check if ither inc or dec
i can sort and check if arrays match or write utils for arrays
two adjacent levels idffer by at least on and at most three

there should be more safe reports
dampener can tolerate a sinlge bad level

we need to try removing a level and check
there are only 5 levels in a row, so try removing each one
'''
lines = open("puzzle.txt", "r")

def check_inc(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
        elif arr[i] - arr[i-1] not in [1,2,3]:
            return False
    return True

def check_dec(arr):
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            return False
        elif arr[i-1] - arr[i] not in [1,2,3]:
            return False
    return True

safe = 0
for l in lines:
    l = list(map(int, l.strip("\n").split(" ")))
    if check_inc(l) or check_dec(l):
        safe += 1
    else:
        #try removing
        for i in range(len(l)):
            new_l = l[:i] + l[i+1:]
            if check_inc(new_l) or check_dec(new_l):
                safe += 1
                break

print(safe)