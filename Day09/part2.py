'''
input is file block
digits alternate between length of file and length of free sapce
each fild on disk has ID number
file and then . as free space
each file has ID number
we need to decode the file into the right represntation
line is 20000 chars lone

once we create the disk we need to move file blocks one at a time, from the end of the disk to the left most free space
we can rotate using two pointers

then compute checksum

for part 2, insteaf of swapping file by file, attempt to fit the whole file to the left most space
in decreasing file order, file only moves if there's enough space, my god what a nightmare of a problem

i now need to know the gaps of dots between files
i can store the gaps of dots as intervals of indices

for file ids, hashmap to group of indices

we cant just skip the block if there'a free space, we might be able to come back to it
'''
from collections import defaultdict
line = open("puzzle.txt","r")
lines = []
for l in line:
    lines.append(l)

line = lines[0]
#recrete the disk format
disk = []
curr_file_id = 0
for i in range(len(line)):
    #id first
    if i % 2 == 0:
        file_length = int(line[i])
        for _ in range(file_length):
            disk.append(str(curr_file_id))
        curr_file_id += 1
    else:
        free_space = int(line[i])
        for _ in range(free_space):
            disk.append(".")

dot_idxs = []
cur_interval = []
for i,char in enumerate(disk):
    if char == '.':
        cur_interval.append(i)
    else:
        if cur_interval:
            dot_idxs.append(cur_interval)
            cur_interval = []

if cur_interval:
    dot_idxs.append(cur_interval)

#mapp file_ids to [idxs]
mapp = defaultdict(list)
for i,ch in enumerate(disk):
    if ch != '.':
        mapp[ch].append(i)

max_file_id = int(max(mapp.keys()))
for file in range(max_file_id,-1,-1):
    print(file)
    #check if we can swap these dots with this file block, this check it at least fits
    #search dot idxs for best while
    can_find = False
    for left in range(len(dot_idxs)):
        if len(dot_idxs[left]) >= len(mapp[str(file)]):
            can_find = True
            break
    if can_find:
        curr_dot_idxs = dot_idxs[left]
        curr_file_idxs = mapp[(str(file))]
        while len(curr_file_idxs) > 0:
            i,j = curr_dot_idxs.pop(0),curr_file_idxs.pop(0)
            if i >= j:
                break
            disk[i],disk[j] = disk[j],disk[i]

check_sum = 0
for i,ch in enumerate(disk):
    if ch != '.':
        check_sum += i*int(ch)
print(check_sum)