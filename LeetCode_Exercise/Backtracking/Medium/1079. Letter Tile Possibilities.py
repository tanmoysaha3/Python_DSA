from collections import Counter


def numTilePossibilities1(self, tiles: str) -> int:
    n=len(tiles)
    res=[0]
    tiles = "".join(sorted(tiles))
    visitedC=set()
    def backTC(index, subset):
        y=tuple(subset[:])
        if(y in visitedC):
            return
        if(index==n):
            if(len(subset)>1):
                visitedC.add(y)
                backTP(0,subset)
            elif(len(subset)==1):
                visitedC.add(y)
                res[0]+=1
            return
        subset.append(tiles[index])
        backTC(index+1, subset)
        subset.pop()
        backTC(index + 1, subset)

    def backTP(index,subset):
        if (index == len(subset) - 1):
            res[0]+=1
            return
        visited = set()
        for j in range(index, len(subset)):
            if (subset[j] not in visited):
                visited.add(subset[j])
                subset[index], subset[j] = subset[j], subset[index]
                backTP(index + 1,subset)
                subset[index], subset[j] = subset[j], subset[index]
    backTC(0,[])
    #print(res)
    return res[0]

tiles = "ABCDEF"
print(numTilePossibilities1(0,tiles))


# Slightly optimized
def numTilePossibilities2(self, tiles: str) -> int:
    res=[0]
    tiles = "".join(sorted(tiles))
    def backTC(index, subset):
        if(len(subset)>1):
            backTP(0,subset)
        elif(len(subset)==1):
            res[0]+=1
        visited = set()
        for j in range(index, len(tiles)):
            if (tiles[j] not in visited):
                visited.add(tiles[j])
                subset.append(tiles[j])
                backTC(j + 1, subset)
                subset.pop()

    def backTP(index,subset):
        if (index == len(subset) - 1):
            res[0]+=1
            return
        visited = set()
        for j in range(index, len(subset)):
            if (subset[j] not in visited):
                visited.add(subset[j])
                subset[index], subset[j] = subset[j], subset[index]
                backTP(index + 1,subset)
                subset[index], subset[j] = subset[j], subset[index]
    backTC(0,[])
    #print(res)
    return res[0]

tiles = "ABCDEF"
print(numTilePossibilities2(0,tiles))


# Using Counter
def numTilePossibilities3(self, tiles: str) -> int:
    Count = Counter(tiles)

    def backT():
        res=0
        for c in Count:
            if(Count[c]>0):
                # include
                Count[c]-=1
                res+=1
                res+=backT()
                # backtrack
                Count[c]+=1
        return res
    return backT()

tiles = "ABCDEF"
print(numTilePossibilities3(0,tiles))