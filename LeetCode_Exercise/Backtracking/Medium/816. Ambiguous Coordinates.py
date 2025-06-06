from decimal import Decimal
from typing import List


def ambiguousCoordinates1(self, s: str) -> List[str]:
    x = []
    for j in range(2, len(s) - 1):
        a = s[:j]
        b = s[j:]
        m = []
        if (len(str(int(a[1:]))) == len(a[1:])):
            m.append(a)
        for k in range(2, len(a), 1):
            f = a[:k] + "." + a[k:]
            if (str(Decimal(f[1:]).normalize()) == f[1:]):
                m.append(f)
        n = []
        if (len(str(int(b[:-1]))) == len(b[:-1])):
            n.append(b)
        for k in range(1, len(b) - 1, 1):
            g = b[:k] + '.' + b[k:]
            if (str(Decimal(g[:-1]).normalize()) == g[:-1]):
                n.append(g)
        z = [p + ", " + q for q in n for p in m]
        x.extend(z)
    return x

s = "(0000001)"
print(ambiguousCoordinates1(0,s))


# Optimized - not really a backtracking
def ambiguousCoordinates2(self, s: str) -> List[str]:
    res = []

    def backT(index, subset, temp):
        if (index == len(subset) or subset[-1] == "0"):
            if (subset == "0" or subset[0] != "0"):
                temp.append(subset)
            return
        temp.append(subset[:index] + "." + subset[index:])
        if (subset[0] == "0"):
            return
        backT(index + 1, subset, temp)

    for j in range(2, len(s) - 1):
        a = s[1:j]
        b = s[j:-1]
        m = []
        n = []
        backT(1, a, m)
        backT(1, b, n)
        z = ["(" + p + ", " + q + ")" for q in n for p in m]
        res.extend(z)
    return res

s = "(0000001)"
print(ambiguousCoordinates2(0,s))