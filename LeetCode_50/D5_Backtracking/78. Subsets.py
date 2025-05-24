#                       []
#          []                          [1]
#    []         [2]            [1]            [1,2]
#  []  [3]   [2]   [2,3]    [1]   [1,3]   [1,2]    [1,2,3]


from typing import List


def subsets(self, nums: List[int]) -> List[List[int]]:
    output=[]
    def backT(nums, i, subset):
        if(i==len(nums)):
            output.append(subset[:])
            return
        #exclude
        backT(nums, i+1, subset)
        #include
        subset.append(nums[i])
        backT(nums, i+1, subset)
        subset.pop()
        #include
    backT(nums,0, [])
    return output

nums = [1,2,3]
print(subsets(0,nums))