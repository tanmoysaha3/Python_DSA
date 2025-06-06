from typing import List


def splitIntoFibonacci(self, num: str) -> List[int]:
    n = len(num)
    res = []

    def backT(index, subset):
        if (subset[0] == num or index < 0 or int(subset[-1]) >= 2 ** 31):
            return False
        if (index == 0):
            res[:] = subset[::-1]
            return True
        if (len(subset) == 1):
            for i in range(len(subset[-1])):
                x = num[index - i - 1:index]
                if (x == ""):
                    break
                z = str(int(subset[-1]) - int(x))
                if (num[:index - i - 1].endswith(z)):
                    if (len(z) == 1 or (not z.startswith("0"))) and (len(x) == 1 or (not x.startswith("0"))):
                        subset.append(x)
                        if (backT(index - i - 1, subset)):
                            return True
                        subset.pop()

            index -= 1
            subset[-1] = num[index] + subset[-1]
            while (subset[-1][0] == "0" and index > 0):
                index -= 1
                subset[-1] = num[index] + subset[-1]
            if (backT(index, subset)):
                return True
        else:
            z = str(int(subset[-2]) - int(subset[-1]))
            if (num[:index].endswith(z)):
                subset.append(z)
                if (backT(index - len(z), subset)):
                    return True
                subset.pop()
        return False

    backT(n - 1, [num[-1]])
    for i in range(len(res)):
        res[i] = int(res[i])
    return res

num = "1101111"
print(splitIntoFibonacci(0,num))