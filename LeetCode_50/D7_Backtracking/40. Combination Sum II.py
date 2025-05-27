from typing import List


def combinationSum2_1(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res=[]
    def backT(i,subset):
        if(sum(subset)==target):
            res.append(subset[:])
            return
        if(sum(subset)>target):
            return
        visited=set()
        for j in range(i, len(candidates)):
            if(candidates[j] not in visited):
                visited.add(candidates[j])
                subset.append(candidates[j])
                backT(j+1, subset)
                subset.pop()
    backT(0,[])
    return res

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,33,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,44,4,4,4,5,5,5,5,5,5,5,5,5,5,5,49,5,5,5,5,6,6,6,6]
target = 29
print(combinationSum2_1(0,candidates, target))

#Slight improvement
def combinationSum2_2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res = []
    n = len(candidates)

    def backT(i, subset, sumT):
        if (sumT == target):
            res.append(subset[:])
            return
        if (sumT > target):
            return
        visited = set()
        for j in range(i, n):
            if (candidates[j] not in visited):
                visited.add(candidates[j])
                subset.append(candidates[j])
                backT(j + 1, subset, sumT + candidates[j])
                subset.pop()

    backT(0, [], 0)
    return res