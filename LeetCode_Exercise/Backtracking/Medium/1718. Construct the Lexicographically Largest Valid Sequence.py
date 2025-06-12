from typing import List

# Need Rethink
def constructDistancedSequence(self, n: int) -> List[int]:
    res = [0]*(2*n-1)
    used = set()

    def backT(index):
        if(index==len(res)):
            return True

        for num in reversed(range(1,n+1)):
            if(num in used):
                continue
            if(num>1 and (index+num >= len(res) or res[index+num])):
                continue
            used.add(num)
            if(num==1):
                res[index] = num
            else:
                res[index] = num
                res[index+num] = num
            j=index+1
            while(j<len(res) and res[j]):
                j+=1
            if(backT(j)):
                return True

            used.remove(num)
            res[index]=0
            if(num>1):
                res[index+num]=0
        return False
    backT(0)
    return res

print(constructDistancedSequence(0,3))