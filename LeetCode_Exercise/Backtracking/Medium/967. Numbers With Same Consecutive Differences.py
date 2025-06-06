from typing import List


def numsSameConsecDiff1(self, n: int, k: int) -> List[int]:
    res=set()
    def backT(index, subset):
        if(len(subset)==n):
            res.add(int(subset))
            return
        subset+=str(index)
        if(index+k<10):
            backT(index+k,subset)
        if(index-k>=0):
            backT(index-k,subset)
    for i in range(1,10):
        backT(i,"")
    return list(res)

n = 3
k = 7
print(numsSameConsecDiff1(0,n,k))


# Slight Change
def numsSameConsecDiff2(self, n: int, k: int) -> List[int]:
    res = []

    def backT(index, subset):
        if (len(subset) >= n):
            res.append(int(subset))
            return
        if (index + k < 10):
            backT(index + k, subset + str(index + k))
        if (index - k >= 0 and k != 0):
            backT(index - k, subset + str(index - k))

    for i in range(1, 10):
        backT(i, str(i))
    return list(res)

n = 3
k = 7
print(numsSameConsecDiff2(0,n,k))
