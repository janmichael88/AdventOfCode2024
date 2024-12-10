from collections import defaultdict

'''
two lists, left and right, sort them and sum absolute differend
'''
lines = open("puzzle.txt","r")
split_delim = "   "
left,right = [],[]
for l in lines:
    l = l.strip("\n")
    temp = l.split(split_delim)
    left.append(int(temp[0]))
    right.append(int(temp[1]))

left.sort()
right.sort()

total_distance = 0
for l,r in zip(left,right):
    total_distance += abs(l - r)

print(total_distance)
