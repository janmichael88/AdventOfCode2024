'''
given equations
ans: numbers, can only use + and *
determine if we can use numbers to make it true

brute force and try all possibl + *
recusrively using backtracking or power set
ops are always evaluated left to right, not order of precendence
'''
lines = open("puzzle.txt","r")

#functino to try + and *
#0 is + an 1 is *
def f(arr,ans):
    n = len(arr)
    for mask in range(1 << (n-1)):
        start = arr[0]
        for i in range(n-1):
            #if 1 multiply
            if (mask & (1 << i)) == 0:
                start += arr[i+1]
            else:
                start *= arr[i+1]
        if start == ans:
            return True
    
    return False

total_calibration = 0
for l in lines:
    ans,nums = l.strip().split(":")
    ans = int(ans.strip())
    nums = nums.strip()
    nums = list(map(int, [num for num in nums.split(" ")]))
    if f(nums,ans):
        total_calibration += ans

print(total_calibration)