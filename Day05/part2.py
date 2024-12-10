'''
first half of puzzle is graph
u|v
generate graph, 

for part 2, generate the correct ordering if the inital ordering is incorrect
after reordering, get the middle numbers again (but only for the reorded incorrect orderings)

frame the problem as,
    say we have a DAG with some subset of nodes in DAG containting (a,b,c)
    find ordering for this dag

find topolgoical ordering of graph, then mapp to ordered index, then mapp again
input can have cycles! so its not a DAG
even though its correclty ordered we can still try to follow the path

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
    if not follow_path(o,graph):
        orignums = o[:]
        badone = True
        while badone:
            badone = False
            for i in range(1, len(o)):
                if not o[i] in graph[o[i-1]]:
                    o[i], o[i-1] = o[i-1], o[i]
                    badone = True
        if not orignums == o:
            ans += int(o[len(o)//2])

print(ans)
