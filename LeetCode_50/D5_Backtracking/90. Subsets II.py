from typing import List


def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    output=[]
    def backT(i,subset):
        if(i==len(nums)):
            output.append(subset[:])
            return
        #include
        subset.append(nums[i])
        backT(i+1,subset)
        subset.pop()
        #exclude
        while(i<len(nums)-1 and nums[i]==nums[i+1]):
            i+=1
        backT(i+1, subset)

    backT(0, [])
    return output

nums = [1,2,2]
print(subsetsWithDup(0,nums))