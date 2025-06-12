def punishmentNumber1(self, n: int) -> int:
    res = []

    def backT(index, subset, str_n, n):
        if (index >= len(str_n)):
            if (sum(int(i) for i in subset) == n):
                return True
            return
        for i in range(len(str_n) - index):
            subset.append(str_n[index:index + i + 1])
            if (backT(index + i + 1, subset, str_n, n)):
                return True
            subset.pop()
        return False

    for i in range(1, n + 1):
        if (backT(0, [], str(i ** 2), i)):
            res.append(i)
    # print(res)
    res_sum = 0
    for i in res:
        res_sum += i ** 2
    return res_sum

n=10
print(punishmentNumber1(0,n))


# Slight Optimized
def punishmentNumber2(self, n: int) -> int:
    res = []

    def backT(index, str_n, n, sum_n, z):
        if (index >= z):
            if (sum_n == n):
                return True
            return
        for i in range(z - index):
            if (backT(index + i + 1, str_n, n, sum_n + int(str_n[index:index + i + 1]), z)):
                return True
        return False

    for i in range(1, n + 1):
        y = str(i ** 2)
        if (backT(0, y, i, 0, len(y))):
            res.append(i)
    res_sum = 0
    for i in res:
        res_sum += i ** 2
    return res_sum

n=10
print(punishmentNumber2(0,n))