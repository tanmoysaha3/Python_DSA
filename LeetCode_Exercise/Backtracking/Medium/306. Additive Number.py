# Backward Direction
def isAdditiveNumber1(self, num: str) -> bool:
    n = len(num)

    def backT(index, subset):
        if (subset[0] == num or index<0):
            return False
        if(index==0):
            return True
        if(len(subset)==1):
            for i in range(len(subset[-1])):
                x = num[index - i - 1:index]
                if(x==""):
                    break
                z = str(int(subset[-1]) - int(x))
                if (num[:index - i - 1].endswith(z)):
                    if (len(z) == 1 or (not z.startswith("0"))) and (len(x) == 1 or (not x.startswith("0"))):
                        subset.append(x)
                        if(backT(index - i - 1, subset)):
                            return True
                        subset.pop()

            index-=1
            subset[-1]=num[index]+subset[-1]
            while (subset[-1][0] == "0" and index>0):
                index-=1
                subset[-1] = num[index] + subset[-1]
            if(backT(index, subset)):
                return True
        else:
            z = str(int(subset[-2]) - int(subset[-1]))
            if (num[:index].endswith(z)):
                subset.append(z)
                if(backT(index-len(z), subset)):
                    return True
                subset.pop()
        return False
    return backT(n - 1, [num[-1]])

print(isAdditiveNumber1(0, "199001200"))

# Forward Direction
def isAdditiveNumber2(self, num: str) -> bool:
    if (len(num) < 3):
        return False

    def backT(first, second, remaining):
        if (len(remaining) < max(len(first), len(second))):
            return False

        if ((first[0] == '0' and len(first) > 1) or (second[0] == "0" and len(second) > 1)):
            return False

        res = str(int(first) + int(second))
        if (len(remaining) < len(res)):
            return False

        if (res == remaining[0:len(res)]):
            if (len(res) == len(remaining)):
                return True
            first = second
            second = res
            remaining = remaining[len(res):]
            return backT(first, second, remaining)

        return False

    for i in range(1, len(num)):
        for j in range(i + 1, len(num)):
            first = num[0:i]
            second = num[i:j]
            remaining = num[j:]
            if (backT(first, second, remaining)):
                return True
    return False

print(isAdditiveNumber2(0, "199001200"))