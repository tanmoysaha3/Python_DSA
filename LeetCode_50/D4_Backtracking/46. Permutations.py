import itertools
from typing import List

#Normal Solution
def permute1(self, nums: List[int]) -> List[List[int]]:
    x=[list(p) for p in itertools.permutations(nums)]
    return x

nums = [1,2,3]
print(permute1(0,nums))

#Backtracking
def permute2(self, nums: List[int]) -> List[List[int]]:
    n=len(nums)
    res=[]
    def backT(index):
        if(index==n-1):
            res.append(nums[:])
            return
        for j in range(index,n):
            nums[index], nums[j]=nums[j],nums[index]
            backT(index+1)
            nums[index], nums[j] = nums[j], nums[index]
    backT(0)
    return res
