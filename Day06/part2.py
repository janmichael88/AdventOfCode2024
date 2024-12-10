'''
we need to find the (i,j) that cause the guard to get stuck in a loop
and return the number of (i,j)s the cause it
brute force would be try all i,j and see if the guard gets stuck
cubic time seems reasonable for this

even if there weren't a loop, some cells would be revisited
***
key intuition:
if i were to ever revisit a cell (i,j) in going in the same direction more than once, then i'd be caught in a loop!
***

so try all (i,j)
and if i come back to this same spot in the same direction, then were in a loop
'''
from collections import Counter
lines = open("sample.txt","r")
grid = []
for l in lines:
    l = l.strip()
    grid.append(list(l))

#find start
rows,cols = len(grid), len(grid[0])
start_i,start_j = -1,-1

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '^':
            start_i, start_j = i,j
            break

#make this into functino for part2
def in_loop(start_i,start_j,curr_dir,dirrs,grid,visited):
    #keep going while in bounds
    while (0 <= start_i < rows) and (0 <= start_j < cols):
        if (start_i,start_j,curr_dir) in visited:
            return True
        visited.add((start_i,start_j,curr_dir))
        di,dj = dirrs[curr_dir]
        #in bounds and can walk to
        if (0 <= start_i + di < rows) and (0 <= start_j + dj < cols) and (grid[start_i + di][start_j + dj] == '.'):
            start_i = start_i + di
            start_j = start_j + dj
        elif (0 <= start_i + di < rows) and (0 <= start_j + dj < cols) and (grid[start_i + di][start_j + dj] == '#'):
            curr_dir = (curr_dir + 1) % 4
            di,dj = dirrs[curr_dir]
            start_i = start_i + di
            start_j = start_j + dj
        elif (start_i + di < 0) or (start_i + di >= rows) or (start_j + dj < 0) or (start_j + dj >= cols):
            break
    
    return False

obstacles = 0
dirrs = [[-1,0],[0,1],[1,0],[0,-1]]
for i in range(rows):
    for j in range(cols):
        if (i,j) == (start_i,start_j):
            continue
        if grid[i][j] == '.':
            print(i,j)
            #make in wall
            grid[i][j] = '#'
            grid[start_i][start_j] = '.'
            curr_dir = 0
            visited = set()
            if in_loop(start_i,start_j,curr_dir,dirrs,grid,visited):
                obstacles += 1
            #change back
            grid[i][j] = '.'

print(obstacles)


            
