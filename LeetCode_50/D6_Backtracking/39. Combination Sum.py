from typing import List


def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
    res=[]
    def backT(i, subset):
        if(sum(subset)==target):
            res.append(subset[:])
            return
        if(sum(subset)>target):
            return

        for j in range(i,len(candidates)):
            #print(subset,j)
            subset.append(candidates[j])
            backT(j,subset)
            subset.pop()
    backT(0,[])
    return res

candidates = [2,3,6,7]
target = 7
print(combinationSum1(0,candidates, target))

#Slight improvement
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    n = len(candidates)

    def backT(i, subset, sumT):
        if (sumT == target):
            res.append(subset[:])
            return
        elif (sumT > target):
            return

        for j in range(i, n):
            # print(subset,j)
            subset.append(candidates[j])
            backT(j, subset, sumT + candidates[j])
            subset.pop()

    backT(0, [], 0)
    return res

print(combinationSum2(0,candidates, target))