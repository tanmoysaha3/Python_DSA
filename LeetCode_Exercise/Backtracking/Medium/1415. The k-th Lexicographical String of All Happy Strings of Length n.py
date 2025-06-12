def getHappyString1(self, n: int, k: int) -> str:
    res=[]
    def backT(index,subset):
        if(index==n-1):
            res.append(subset[:])
            return
        if(subset[-1]=="a"):
            backT(index+1, subset+"b")
            backT(index+1, subset+"c")
        elif(subset[-1]=='b'):
            backT(index+1, subset+"a")
            backT(index+1, subset+"c")
        elif(subset[-1]=="c"):
            backT(index+1, subset+"a")
            backT(index+1, subset+"b")
    backT(0,"a")
    backT(0, "b")
    backT(0, "c")
    print(res)
    if(k>len(res)):
        return ""
    else:
        return res[k-1]

n = 1
k = 4
print(getHappyString1(0,n,k))


#Optimized but not backtracking
def getHappyString2(self, n: int, k: int) -> str:
    total_happy = 3*(2**(n-1))

    res=[]
    choices="abc"
    left, right = 1, total_happy

    for i in range(n):
        curr = left
        partition_size = (right-left+1)//len(choices)

        for c in choices:
            if(k in range(curr, curr+partition_size)):
                res.append(c)
                left=curr
                right=curr+partition_size
                choices="abc".replace(c,"")
                break
            curr+=partition_size

    return "".join(res)

n = 3
k = 4
print(getHappyString2(0,n,k))