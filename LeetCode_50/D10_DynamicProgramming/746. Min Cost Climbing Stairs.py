from typing import List


# Recursion - TLE
def minCostClimbingStairs(self, cost: List[int]) -> int:
    res = [999000]

    def rec(index, z):
        if (index == len(cost) and z < res[0]):
            res[0] = z
            return
        if (index > len(cost) or z >= res[0]):
            return
        rec(index + 1, z + cost[index])
        rec(index + 2, z + cost[index])

    rec(0, 0)
    rec(1, 0)
    return res[0]

#cost = [10,15,20]
#print(minCostClimbingStairs(0,cost))


# Memorization
def minCostClimbingStairsM(self, cost: List[int]) -> int:
    dp=[-1]*len(cost)
    def rec(index):
        if (index >= len(cost)):
            return 0
        if(dp[index]!=-1):
            return dp[index]
        dp[index]=min(rec(index + 1)+cost[index],rec(index + 2)+cost[index])
        return dp[index]
    return min(rec(0), rec(1))

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairsM(0,cost))


# Tabulation + Space Optimized
def minCostClimbingStairsT(self, cost: List[int]) -> int:
    prev=0
    curr=0
    cout=2
    while(cout<=len(cost)):
        prev, curr = curr, min(prev+cost[cout-2], curr+cost[cout-1])
        cout+=1
    return curr

cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairsT(0,cost))