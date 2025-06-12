def nextBeautifulNumber(self, n: int) -> int:
    res=[]
    def backT(index,subset):
        print(index,subset)
        if(len(subset)>len(str(n)) or index>len(str(n))+1):
            if(len(subset)==len(str(n))+1):
                res.append(subset)
            return
        if (len(subset) == len(str(n))):
            res.append(subset)
            return
        backT(index+1, subset+(str(index)*index))
        backT(index+1, subset)
    backT(1,"")
    print(res)

    full_res = []

    def backTP(index, subset):
        if (index == len(subset) - 1):
            #full_res.append(subset[:])
            full_res.append(int("".join(subset)))
            return
        visited = set()
        for j in range(index, len(subset)):
            if (subset[j] not in visited):
                visited.add(subset[j])
                subset[index], subset[j] = subset[j], subset[index]
                backTP(index + 1,subset)
                subset[index], subset[j] = subset[j], subset[index]

    #backTP(0)

    for i in range(len(res)):
        print(list(res[i]))
        backTP(0,list(res[i]))
    print(full_res)
    full_res.sort()
    for i in full_res:
        if(i>n):
            return i
    return 0

print(nextBeautifulNumber(0,1000000))