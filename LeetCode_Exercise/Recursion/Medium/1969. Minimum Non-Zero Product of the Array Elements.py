#Non Recursive Solution
def minNonZeroProduct(self, p: int) -> int:
    MOD = 10 ** 9 + 7
    x = pow(2, p)
    return pow((x - 2), ((x // 2) - 1), MOD) * (x % MOD - 1) % MOD