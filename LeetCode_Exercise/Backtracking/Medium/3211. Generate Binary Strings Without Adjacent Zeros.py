from typing import List


def validStrings(self, n: int) -> List[str]:
    res=[]
    def backT(index,subset):
        if(index==n):
            res.append(subset)
            return
        if(subset[-1]=="1"):
            backT(index + 1, subset + "1")
            backT(index + 1, subset + "0")
        else:
            backT(index + 1, subset + "1")
    backT(1, "1")
    backT(1, "0")
    return res

n = 18
print(validStrings(0,n))