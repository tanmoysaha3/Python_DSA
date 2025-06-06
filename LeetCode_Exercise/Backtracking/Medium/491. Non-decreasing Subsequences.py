from typing import List


def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    visited = set()

    def backT(index, subset):
        if (index == len(nums)):
            if (len(subset) > 1):
                visited.add(tuple(subset))
            return

        if (len(subset) == 0 or subset[-1] <= nums[index]):
            subset.append(nums[index])
            backT(index + 1, subset)
            subset.pop()
        backT(index + 1, subset)

    backT(0, [])
    return list(visited)

nums = [100,90,80,70,60,50,60,70,80,90,100]
print(findSubsequences(0,nums))