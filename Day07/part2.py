'''
given equations
ans: numbers, can only use + and *
determine if we can use numbers to make it true

brute force and try all possibl + *
recusrively using backtracking or power set
ops are always evaluated left to right, not order of precendence

part 2, same is part 1, but we have one more operation, the concat operation
we can still brute force it, but it might take longer
recursively generate the operations

i can either do recursivele or base 3
'''
lines = open("puzzle.txt","r")

#functino to try + and *
#0 is + an 1 is *


#recursively gnerate ops
def f(n,path,arr,ans):
    all_ops = []
    def rec(n,path):
        if len(path) >= n:
            if path:
                all_ops.append(path[:])
            return
        for o in ["+","*","||"]:
            rec(n,path +[o])
    rec(n,path)
    #evaluate
    for ops in all_ops:
        start = arr[0]
        for i in range(len(ops)):
            if ops[i] == '+':
                start += arr[i+1]
            elif ops[i] == '*':
                start *= arr[i+1]
            else:
                start = int(str(start) + str(arr[i+1]))
        
        if start == ans:
            return True
    return False

#print(f(2,[]))
total_calibration = 0
for i,l in enumerate(lines):
    print(i)
    ans,nums = l.strip().split(":")
    ans = int(ans.strip())
    nums = nums.strip()
    nums = list(map(int, [num for num in nums.split(" ")]))
    n = len(nums) - 1
    if f(n,[],nums,ans):
        total_calibration += ans

print(total_calibration)
