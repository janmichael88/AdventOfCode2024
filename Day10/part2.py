'''
dfs from all 0 cells,
for each neighbor cell, we can only go up down left and right and the cell must be one greater
score of a trail head is the number of 9s, once we get to a nine we are done

careful, its not the number of 9s that you hit, its the unique 9's

part2, new hueristic called rating
'''
lines = open("puzzle.txt","r")
grid = []
for l in lines:
    l = l.strip()
    grid.append(l)

rows, cols = len(grid), len(grid[0])
zeros = []
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '0':
            zeros.append((i,j))

def dp(i,j,grid,rows,cols,seen):
    if grid[i][j] == '9':
        return 1
    seen.add((i,j)) 
    dirrs = [[1,0],[-1,0],[0,1],[0,-1]]
    ans = 0
    for di,dj in dirrs:
        ii = i + di
        jj = j + dj
        if 0 <= ii < rows and 0 <= jj < cols and (ii,jj) not in seen:
            if grid[ii][jj] == '.':
                continue
            if int(grid[ii][jj]) - int(grid[i][j]) == 1:
                ans += dp(ii,jj,grid,rows,cols,seen)
    seen.remove((i,j))
    return ans

score = 0
for i,j in zeros:
    seen = set()
    rating = dp(i,j,grid,rows,cols,seen)
    score += rating

print(score)