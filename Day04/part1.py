'''
word search for XMAS
pick cell (i,j) and look in all 8 directions for XMAS
'''

lines = open("sample.txt","r")
arr = []

for l in lines:
    arr.append(l.strip("\n"))

rows,cols = len(arr),len(arr[0])
target_word = "XMAS"

ans = 0
for i in range(rows):
    for j in range(cols):
        if arr[i][j] == 'X':
            #up,down,left,right
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)):
                if 0 <= i + 3*di < rows and 0 <= j + 3*dj < cols:
                    suffix = ""
                    for k in range(1,4):
                        suffix += arr[i + k*di][j + k*dj]
                    
                    if suffix == 'MAS':
                        ans += 1


print(ans)