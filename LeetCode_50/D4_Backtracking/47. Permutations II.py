from typing import List


def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    n=len(nums)
    res=[]
    def backT(index):
        if(index==n-1):
            res.append(nums[:])
            return
        visited = set()
        for j in range(index,n):
            if(nums[j] not in visited):
                visited.add(nums[j])
                nums[index], nums[j] = nums[j], nums[index]
                backT(index+1)
                nums[index], nums[j] = nums[j], nums[index]

    backT(0)
    return res

nums = [1,1,2]
print(permuteUnique(0,nums))