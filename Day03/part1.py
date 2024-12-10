import re

'''
regex and capture mul
'''

lines = open("puzzle.txt","r")
capture_pattern = r"mul\((\d+),(\d+)\)"

ans = 0
for l in lines:
    l = re.findall(capture_pattern,l)
    for t in l:
        first,second = int(t[0]), int(t[1])
        ans += first*second

print(ans)
