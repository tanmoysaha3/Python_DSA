from functools import cache
from typing import List


def canPartitionR(self, nums: List[int]) -> bool:
    y=sum(nums)
    x = y // 2
    if(x*2!=y):
        return False

    def rec(index, total):
        if(index==len(nums) or total>=x):
            if(total==x):
                return True
            return False
        if(rec(index+1, total+nums[index])):
            return True
        if (rec(index + 1, total)):
            return True
    return rec(0,0)


def canPartitionM(self, nums: List[int]) -> bool:
    dp = set()
    y = sum(nums)
    x = y // 2
    if (x * 2 != y):
        return False

    def rec(index, total):
        if (index == len(nums) or total >= x):
            if (total == x):
                return True
            return False
        if ((index + 1, total + nums[index]) not in dp):
            if (rec(index + 1, total + nums[index])):
                return True
            else:
                dp.add((index + 1, total + nums[index]))
        if ((index + 1, total) not in dp):
            if (rec(index + 1, total)):
                return True
            else:
                dp.add((index + 1, total))
        return False


def canPartition1(self, nums: List[int]) -> bool:
    dp = {0}
    y = sum(nums)
    x = y // 2
    if (x * 2 != y):
        return False
    for i in range(len(nums)):
        if(nums[i]==x):
            return True
        a=set()
        for j in dp:
            if(j+nums[i]==x):
                return True
            a.add(j+nums[i])
        dp.update(a)
    return False


# Built-in cache instead of Memorization
def canPartition2(self, nums: List[int]) -> bool:
    y = sum(nums)
    x = y // 2
    if (x * 2 != y):
        return False
    @cache
    def dp(index, total):
        if(index==len(nums) or total>=x):
            return total==x
        return dp(index+1, total+nums[index]) or dp(index+1, total)
    return dp(0,0)

nums = [1,2,3,5,17,6,14,12,6]
#print(canPartitionR(0,nums))
#print(canPartitionM(0,nums))
#print(canPartition1(0,nums))
print(canPartition2(0,nums))
