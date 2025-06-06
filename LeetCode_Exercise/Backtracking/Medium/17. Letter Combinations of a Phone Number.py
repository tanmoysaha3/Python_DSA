from itertools import product
from typing import List


#Backtracking
def letterCombinations1(self, digits: str) -> List[str]:
    if (len(digits) == 0):
        return []
    x={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],
       5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],
       8:['t','u','v'],9:['w','x','y','z']}
    res=[]

    def bactT(start,subset):
        if(len(subset)==len(digits)):
            res.append("".join(subset))
            return
        for i in x[int(digits[start])]:
            subset.append(i)
            bactT(start+1, subset)
            subset.pop()


    bactT(0,[])
    return res


#Straight
def letterCombinations2(self, digits: str) -> List[str]:
    if (len(digits) == 0):
        return []
    x = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'],
         "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'],
         "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}

    a = x[digits[0]]
    for i in range(1,len(digits)):
        a = [x + y for x, y in product(a, x[digits[i]])]

    return a

digits = ""
print(letterCombinations1(0,digits))
print(letterCombinations2(0,digits))