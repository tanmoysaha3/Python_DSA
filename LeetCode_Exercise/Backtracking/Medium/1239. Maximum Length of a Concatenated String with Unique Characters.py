from typing import List


def maxLength(self, arr: List[str]) -> int:
    res=[0]
    n=len(arr)
    def backT(index,subset):
        #print(index,subset)
        if(index==n):
            y=len(subset)
            if(y>res[0]):
                res[0]=y
            return
        z=set(arr[index])
        if(len(arr[index])==len(z) and z.isdisjoint(subset)):
            backT(index+1,subset+arr[index])
        backT(index + 1, subset)
    backT(0,"")
    return res[0]

arr = ["un","iq","ue"]
print(maxLength(0,arr))