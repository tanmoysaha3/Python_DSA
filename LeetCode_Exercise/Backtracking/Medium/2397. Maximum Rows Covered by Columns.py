from typing import List


# Not much efficient
def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
    res=0
    x=[]
    p=[]
    a,b = len(matrix), len(matrix[0])
    for i in range(len(matrix)):
        y=set({})
        for j in range(len(matrix[0])):
            if(matrix[i][j]==1):
                y.add(j)
        x.append(y)
        if(len(y)==0):
            res+=1
        elif(len(y)<=numSelect):
            p.append(y)
    print(x)

    z=[]
    def backT(index,subset):
        print(index,subset)
        if(index==b or len(subset)==numSelect):
            f=0
            for i in range(len(p)):
                if(len(p[i]-set(subset))==0):
                    f+=1
            z.append(f)
            # if(len(subset)<=numSelect):
            #     z.append(subset[:])
            return
        subset.append(index)
        backT(index+1, subset)
        subset.pop()
        backT(index + 1, subset)

    backT(0,[])
    print(z)
    return max(z)+res


matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]
numSelect = 2
print(maximumRows(0,matrix,numSelect))