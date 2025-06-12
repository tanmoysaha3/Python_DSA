from typing import List


def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
    x=dict()
    res=[]
    res_s=[0]
    def backT(index, subset, sum_a, sum_res):
        #print(index, subset, sum_a, sum_res)
        if(index==12):
            if(sum_a<=numArrows):
                if(sum_res>res_s[0]):
                    res_s[0]=sum_res
                    res[:]=subset[:]
            return
        # subset.append(index)
        # sum_a+=aliceArrows[index]+1
        # sum_res+=index
        backT(index+1,subset+[aliceArrows[index]+1],sum_a+aliceArrows[index]+1,sum_res+index)
        # subset.pop()
        backT(index+1, subset+[0], sum_a, sum_res)
    backT(0,[],0,0)
    print(res_s)
    res[0] += numArrows - sum(res)
    return res

numArrows = 89
aliceArrows = [3,2,28,1,7,1,16,7,3,13,3,5]
print(maximumBobPoints(0,numArrows,aliceArrows))