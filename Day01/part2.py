from collections import defaultdict,Counter

'''
Calculate a total similarity score by adding up each number in the left list after multiplying 
it by the number of times that number appears in the right list.

its just left num, time count(number in right)

'''
lines = open("puzzle.txt","r")
split_delim = "   "
left,right = [],[]
counts_right = Counter()
for l in lines:
    l = l.strip("\n")
    temp = l.split(split_delim)
    left.append(int(temp[0]))
    counts_right[int(temp[1])] += 1

sim_score = 0
for l in left:
    sim_score += l*counts_right[l]

print(sim_score)