from typing import List


# Normal approach
def maximumEvenSplit(self, finalSum: int) -> List[int]:
    if (finalSum % 2 != 0):
        return []
    res = []
    res_s = 0

    i = 1
    while (res_s <= finalSum):
        y = i * 2
        res_s += y
        res.append(y)
        i += 1
    res[-2] += finalSum - res_s + res[-1]
    return res[:-1]

finalSum = 10**10
print(maximumEvenSplit(0, finalSum))