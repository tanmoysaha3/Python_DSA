from typing import List


#Backtracking - Slower
def subsetXORSum(self, nums: List[int]) -> int:
    n = len(nums)
    x = 0

    def backT(i, xor):
        nonlocal x
        if (i == n):
            x += xor
            return
        backT(i + 1, xor)
        xor = xor ^ nums[i]
        backT(i + 1, xor)

    backT(0, 0)
    return x

nums = [5,1,6]
print(subsetXORSum(0,nums))

#Normal Approach - Math - Faster
