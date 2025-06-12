from collections import defaultdict
from typing import List


def countMaxOrSubsets(self, nums: List[int]) -> int:
    res=defaultdict(int)
    def backT(index, subset):
        if(index==len(nums)):
            res[subset]+=1
            return
        backT(index+1, subset|nums[index])
        backT(index+1, subset)
    backT(0,0)
    return res[max(res)]

nums = [3,1]
print(countMaxOrSubsets(0,nums))