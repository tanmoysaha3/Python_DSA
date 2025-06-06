from typing import List

import sys
sys.setrecursionlimit(2**16+4)
def grayCode1(self, n: int) -> List[int]:
    res=[0]
    z={"0"*n}
    def backT(res,x):
        if(len(res)==2**n):
            return res
        for i in range(n):
            x=x[:i]+str(1-int(x[i]))+x[i+1:]
            if(x not in z):
                res.append(int(x,2))
                z.add(x)
                backT(res, x)
            x=x[:i]+str(1-int(x[i]))+x[i+1:]
    backT(res,"0"*n)
    return res
#print(grayCode(0,16))


#Improved using math (addition in reverse)
#0, 1                          + 2
#0, 1, 3, 2                    + 4
#0, 1, 3, 2, 6, 7, 5, 4        + 8
#0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8
def grayCode2(self, n: int) -> List[int]:
    res = [0, 1]

    def backT(index):
        if (index == n):
            return
        x = 2 ** (index)
        for i in range(x - 1, -1, -1):
            res.append(res[i] + x)
        backT(index + 1)

    backT(1)
    return res

print(grayCode2(0,16))

