'''
first half of puzzle is graph
u|v
generate graph, 

bottom half gives orders 
of those that are in the correct order, we need the middle numbers

build graph and see if we can follow the path
'''
from collections import defaultdict
lines = [l for l in open("puzzle.txt","r")]
idx = -1
for i,l in enumerate(lines):
    if l == "\n":
        idx = i
        break

pages = lines[:idx]
order = lines[idx+1:]

def follow_path(path,graph):
    curr = path[0]
    for neigh in path[1:]:
        if neigh not in graph[curr]:
            return False
        curr = neigh
    return True

graph = defaultdict(set)
for p in pages:
    u,v = p.strip("\n").split("|")
    graph[u].add(v)

ans = 0
for o in order:
    o = o.strip("\n").split(",")
    if follow_path(o,graph):
        ans += int(o[len(o) // 2])

print(ans)



