import sys
from typing import List

sys.setrecursionlimit(2**16+4)
def circularPermutation1(self, n: int, start: int) -> List[int]:
    res = [0]
    z = {"0" * n}

    def backT(res, x):
        if (len(res) == 2 ** n):
            return res
        for i in range(n):
            x = x[:i] + str(1 - int(x[i])) + x[i + 1:]
            if (x not in z):
                res.append(int(x, 2))
                z.add(x)
                backT(res, x)
            x = x[:i] + str(1 - int(x[i])) + x[i + 1:]

    backT(res, "0" * n)
    a=res.index(start)
    b=res[a:]+res[:a]
    return b

n = 3
start = 2
print(circularPermutation1(0,n,start))


def circularPermutation2(self, n: int, start: int) -> List[int]:
    res = [0, 1]

    def backT(index):
        if (index == n):
            return
        x = 2 ** (index)
        for i in range(x - 1, -1, -1):
            res.append(res[i] + x)
        backT(index + 1)

    backT(1)
    a = res.index(start)
    b = res[a:] + res[:a]
    return b

n = 3
start = 2
print(circularPermutation2(0,n,start))
