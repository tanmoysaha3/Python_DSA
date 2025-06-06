from typing import List


def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    res = []

    def backT(i, subset):
        if (sum(subset) == n and len(subset)==k):
            res.append(subset[:])
            return
        if (sum(subset) > n):
            return

        for j in range(i, 10):
            # print(subset,j)
            subset.append(j)
            backT(j+1, subset)
            subset.pop()

    backT(1, [])
    return res

k = 3
n = 7
print(combinationSum3(0,k,n))