from typing import List


def combine1(self, n: int, k: int) -> List[List[int]]:
    res=[]
    def backT(start,subset):
        if(len(subset)==k):
            res.append(subset[:])
            return
        for j in range(start,n+1):
            subset.append(j)
            backT(j+1,subset)
            subset.pop()
    backT(1,[])
    return res


#Optimized
def combine2(self, n: int, k: int) -> List[List[int]]:
    res=[]
    def backT(start,subset):
        if(len(subset)==k):
            res.append(subset[:])
            return
        need = k-len(subset)
        for j in range(start,n-(need-1)+1):
            subset.append(j)
            backT(j+1,subset)
            subset.pop()
    backT(1,[])
    return res

n = 4
k = 2
print(combine2(0,n,k))