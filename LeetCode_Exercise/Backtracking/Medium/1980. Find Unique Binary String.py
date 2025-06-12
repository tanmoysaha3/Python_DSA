from typing import List


def findDifferentBinaryString1(self, nums: List[str]) -> str:
    n=len(nums[0])
    res=[""]
    nums=set(nums)
    def backT(index, subset):
        if(index==n-1):
            if(subset not in nums):
                print(subset)
                res[0]=subset
            return
        backT(index+1, subset+'0')
        backT(index+1, subset+'1')

    backT(0,'0')
    print(res)
    if(res[0]==''):
        backT(0,'1')
    return res[0]

nums = ["111","011","001"]
print(findDifferentBinaryString1(0,nums))


# Optimized
def findDifferentBinaryString2(self, nums: List[str]) -> str:
    n = len(nums[0])
    nums_set = set(nums)

    def backtrack(index, subset):
        if index == n:
            if subset not in nums_set:
                return subset
            return None

        res = backtrack(index + 1, subset + '0')
        if res:
            return res
        return backtrack(index + 1, subset + '1')

    return backtrack(0, '')