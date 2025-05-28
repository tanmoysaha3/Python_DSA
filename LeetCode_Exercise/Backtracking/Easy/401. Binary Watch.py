from typing import List


def readBinaryWatch(self, turnedOn: int) -> List[str]:
    x = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
    res = []

    def backT(start, sub1, sub2):
        if (sum(sub1) > 11 or sum(sub2) > 59 or len(sub1) + len(sub2) > turnedOn):
            return
        if (len(sub1) + len(sub2) == turnedOn):
            res.append(str(sum(sub1)) + ":" + str(sum(sub2)).zfill(2))
            return
        for j in range(start, 10):
            if (j <= 3):
                sub1.append(x[j])
                backT(j + 1, sub1, sub2)
                sub1.pop()
            else:
                sub2.append(x[j])
                backT(j + 1, sub1, sub2)
                sub2.pop()

    backT(0, [], [])
    return res

turnedOn = 1
print(readBinaryWatch(0,turnedOn))