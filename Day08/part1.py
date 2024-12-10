'''
antennas are maked with single lowercase, uppercase, or digits
antinode occurs at any point that is perfeclt in line with two antenna of same freqf
but only when when of the antenna is tice as far away as the other
if we are at some cell (i,j) with freq f and if there is another (ii,jj)
then anti nodes appear on the line slope, two units away
math problem

anitnodes can occur at atenna locations
first find I

hash map letter to each cell
then for each pair for a cell find slope 
    walk slope up and down and add to antinodes
'''
from collections import defaultdict,Counter

lines = open("puzzle.txt","r")
grid = []
for l in lines:
    l = l.strip()
    grid.append(l)

rows = len(grid)
cols = len(grid[0])

antennas = defaultdict(list)
for i in range(rows):
    for j in range(cols):
        if grid[i][j] != ".":
            antennas[grid[i][j]].append((i,j))

def get_anitnodes(pair1,pair2,grid,rows,cols,antinodes):
    x1, y1 = pair1
    x2, y2 = pair2
    dy = y1 - y2
    dx = x1 - x2
    #we can just retraverse the grid and find points the satisfy the quation
    #since we have two points, just make sure the aren't the either pair1 or pair2
    #dammit there can only be two antinodes!
    
    #check up from pair1
    if (0 <= x1 + dx < rows) and (0 <= y1 + dy < cols):
        antinodes.add((x1 + dx, y1 + dy))
    
    #from bottom
    if (0 <= x2 - dx < rows) and (0 <= y2 - dy < cols ):
        antinodes.add((x2 - dx, y2 - dy))

antinodes = set()
for a,cells in antennas.items():
    if len(cells) > 1:
        for i in range(len(cells)):
            for j in range(i+1,len(cells)):
                get_anitnodes(cells[i],cells[j],grid,rows,cols,antinodes)

print(len(antinodes))