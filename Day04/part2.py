'''
now wee need to look for 
M.S
.A.
M.S

look for an 'A', the two diagonals can be written as MAS or SAM
we can search on the interior of the matrix, i.e not first row, last row, first col, last col
first diag can be MS or SM
second daig can be MS or SM
'''

lines = open("puzzle.txt","r")
arr = []

for l in lines:
    arr.append(l.strip("\n"))

rows,cols = len(arr),len(arr[0])

ans = 0
for i in range(1,rows-1):
    for j in range(1,cols-1):
        if arr[i][j] == 'A':
            up_left = arr[i-1][j-1]
            up_right = arr[i-1][j+1]
            down_left = arr[i+1][j-1]
            down_right = arr[i+1][j+1]
            diag1 = up_left+down_right
            diag2 = up_right+down_left
            if (diag1 in ['MS','SM']) and (diag2 in ['MS','SM']):
                ans += 1
            
print(ans)