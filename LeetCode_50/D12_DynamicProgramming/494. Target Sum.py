from collections import defaultdict
from typing import List


# TLE
def findTargetSumWaysR(self, nums: List[int], target: int) -> int:
    x=[0]
    y=len(nums)
    def rec(index, remaining):
        if(index==y):
            if(remaining==0):
                x[0]+=1
            return
        rec(index+1,remaining-nums[index])
        rec(index+1,remaining+nums[index])
    rec(0,target)
    return x[0]


def findTargetSumWaysM(self, nums: List[int], target: int) -> int:
    dp={}
    y = len(nums)

    def rec(index, remaining):
        if((index, remaining) in dp):
            return dp[(index,remaining)]
        if (index == y):
            if (remaining == 0):
                return 1
            else:
                return 0
        dp[(index, remaining)] = rec(index + 1, remaining - nums[index]) + rec(index + 1, remaining + nums[index])
        return dp[(index, remaining)]
    return rec(0, target)


def findTargetSumWaysT1(self, nums: List[int], target: int) -> int:
    z = sum(nums)
    dp = [[0]*(2*z+1) for i in range(len(nums)+1)]

    y={z}
    dp[0][z]=1
    for i in range(1,len(nums)+1):
        a=set()
        print("y",y)
        for j in y:
            z1=j+nums[i-1]
            z2=j-nums[i-1]
            print("z1,z2",z1,z2)
            dp[i][z1] += dp[i-1][j]
            dp[i][z2] += dp[i-1][j]
            a.add(z1)
            a.add(z2)
            print("dp",dp[i])
        y=a
    print(dp)
    if (target > z):
        return 0
    return dp[len(nums)][z + target]


def findTargetSumWaysSoT1(self, nums: List[int], target: int) -> int:
    z = sum(nums)
    prev=[0]*(2*z+1)
    curr=[0]*(2*z+1)
    prev[z] = 1
    y = {z}

    for i in range(1,len(nums)+1):
        curr = [0] * (2 * z + 1)
        a = set()
        for j in y:
            z1 = j + nums[i - 1]
            z2 = j - nums[i - 1]
            curr[z1] += prev[j]
            curr[z2] += prev[j]
            a.add(z1)
            a.add(z2)
        y = a
        prev[:]=curr[:]
        print(curr)
    if (target > z):
        return 0
    return curr[z + target]


def findTargetSumWaysT2(self, nums: List[int], target: int) -> int:
    dp=[defaultdict(int) for i in range(len(nums)+1)]
    dp[0][0]=1
    for i in range(len(nums)):
        for j in dp[i]:
            dp[i+1][j+nums[i]]+=dp[i][j]
            dp[i+1][j-nums[i]]+=dp[i][j]
    return dp[len(nums)][target]


def findTargetSumWaysSoT2(self, nums: List[int], target: int) -> int:
    prev=defaultdict(int)
    prev[0]=1
    for i in range(len(nums)):
        curr=defaultdict(int)
        for j,k in prev.items():
            curr[j+nums[i]]+=k
            curr[j-nums[i]]+=k
        prev=curr
    return prev[target]

nums = [1,1,1,1,1]
target = 3
#print(findTargetSumWaysR(0,nums,target))
#print(findTargetSumWaysM(0,nums,target))
#print(findTargetSumWaysT1(0,nums,target))
#print(findTargetSumWaysSoT1(0,nums,target))
#print(findTargetSumWaysT2(0,nums,target))
print("SoT2",findTargetSumWaysSoT2(0,nums,target))