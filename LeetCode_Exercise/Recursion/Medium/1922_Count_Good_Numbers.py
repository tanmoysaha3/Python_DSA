# using 2 recursion functions
def countGoodNumbers1(self, n: int) -> int:
    def rec1(n):
        if (n == 0):
            return 1
        half = rec1(n // 2) % (10 ** 9 + 7)
        if (n % 2 == 0):
            return half * half
        else:
            return half * half * 5

    def rec2(n):
        if (n == 0):
            return 1
        half = rec2(n // 2) % (10 ** 9 + 7)
        if (n % 2 == 0):
            return half * half
        else:
            return half * half * 4

    if (n % 2 == 0):
        return (rec1(n // 2) * rec2(n // 2)) % (10 ** 9 + 7)
    else:
        return (rec1(n // 2) * rec2(n // 2) * 5) % (10 ** 9 + 7)


# using 1 recursion function
def countGoodNumbers2(self, n: int) -> int:
    MOD = 10 ** 9 + 7

    def rec(n):
        if (n == 0):
            return 1
        half = rec(n // 2) % MOD
        if (n % 2 == 0):
            return half * half
        else:
            return half * half * 5 * 4

    if (n % 2 == 0):
        return (rec(n // 2)) % MOD
    else:
        return (rec(n // 2) * 5) % MOD


n=1000000000000000
print(countGoodNumbers1(0,n))
print(countGoodNumbers2(0,n))