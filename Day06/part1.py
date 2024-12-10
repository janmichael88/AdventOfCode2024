'''
simulation problem
walks up, walks right, walks down, walks left
keep moving guard until it walks off the grid
counlt number of distinct spots guard visites
'''
lines = open("puzzle.txt","r")
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
grid[start_i][start_j] = "."
dirrs = [[-1,0],[0,1],[1,0],[0,-1]]
curr_dir = 0
visited = set()

#keep going while in bounds
while (0 <= start_i < rows) and (0 <= start_j < cols):
    visited.add((start_i,start_j))
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

print(len(visited))





