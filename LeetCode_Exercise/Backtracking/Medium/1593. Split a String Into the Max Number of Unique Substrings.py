def maxUniqueSplit1(self, s: str) -> int:
    res = []
    n = len(s)

    def backT(index, subset):
        if (index == n):
            if ("".join(subset) == s):
                res.append(len(subset))
            return
        for i in range(index, n):
            if (s[index:i + 1] not in subset):
                backT(i + 1, subset + [s[index:i + 1]])

    backT(0, [])
    return max(res)

s = "ababccc"
print(maxUniqueSplit(0,s))


# Optimized
def maxUniqueSplit2(self, s: str) -> int:
    res = 0
    n = len(s)

    def backT(index, subset):
        nonlocal res
        if index == n:
            res = max(res, len(subset))
            return

        for i in range(index, n):
            curr = s[index:i+1]
            if curr not in subset:
                subset.add(curr)
                backT(i + 1, subset)
                subset.remove(curr)

    backT(0, set())
    return res
