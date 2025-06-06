from typing import List


def restoreIpAddresses1(self, s: str) -> List[str]:
    y = len(s)
    if (y > 12 or y < 4):
        return []
    res = set()

    def is_valid_byte(s):
        return (s == "0" or not s.startswith("0")) and 0 <= int(s) <= 255

    def backT(index,subset):
        if(index==len(s) and len(subset)==4):
            x=".".join(subset)
            res.add(x)
            return
        if(index>=len(s) or len(subset)>4):
            return
        for i in range(3):
            z=s[index:index+i+1]
            if (is_valid_byte(z)):
                subset.append(z)
                backT(index+i+1, subset)
                subset.pop()
    backT(0,[])
    return list(res)

s = "101023"
print(restoreIpAddresses1(0,s))


#Normal way
def restoreIpAddresses2(self, s: str) -> List[str]:
    y = len(s)
    if (y > 12 or y < 4):
        return []
    res = set()
    for i in range(3):
        if ((s[:i + 1].startswith('0') and len(s[:i + 1]) > 1) or int(s[:i + 1]) > 255):
            break
        for j in range(i + 1, min(i + 4, y)):
            if ((s[i + 1:j + 1].startswith('0') and len(s[i + 1:j + 1]) > 1) or int(s[i + 1:j + 1]) > 255):
                break
            for k in range(j + 1, min(j + 4, y)):
                if ((s[j + 1:k + 1].startswith('0') and len(s[j + 1:k + 1]) > 1) or int(s[j + 1:k + 1]) > 255):
                    break
                for l in range(k + 1, min(k + 4, y)):
                    if ((s[k + 1:].startswith('0') and len(s[k + 1:]) > 1) or int(s[k + 1:]) > 255):
                        break
                    x = s[:i + 1] + '.' + s[i + 1:j + 1] + '.' + s[j + 1:k + 1] + '.' + s[k + 1:]
                    res.add(x)
    return list(res)

s = "101023"
print(restoreIpAddresses2(0,s))


# Slight change in indexing in backtrack
def restoreIpAddresses3(self, s: str) -> List[str]:
    y = len(s)
    if (y > 12 or y < 4):
        return []
    res = []

    def is_valid_byte(s):
        return (s == "0" or not s.startswith("0")) and 0 <= int(s) <= 255

    def backT(index,subset):
        if(index==len(s) and len(subset)==4):
            x=".".join(subset)
            res.append(x)
            return
        for i in range(index,min(index+3,y)):
            z=s[index:i+1]
            if (is_valid_byte(z)):
                subset.append(z)
                backT(i+1, subset)
                subset.pop()
    backT(0,[])
    return res

s = "101023"
print(restoreIpAddresses3(0,s))