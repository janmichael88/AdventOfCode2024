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
'''

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

left = 0
right = len(disk) - 1
while left <= right:
    while disk[left] == '.' and disk[right] != '.':
        disk[left],disk[right] = disk[right],disk[left]
        left += 1
        right -= 1
    
    #find next points
    while disk[left] != '.':
        left += 1
    while disk[right] == '.':
        right -= 1
    
check_sum = 0
left = 0
while left < len(disk) and disk[left] != '.':
    check_sum += left*(int(disk[left]))
    left += 1

print(check_sum)