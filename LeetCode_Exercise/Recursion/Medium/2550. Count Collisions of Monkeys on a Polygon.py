n = 500000003

def monkeyMove(self, n: int) -> int:
    def rec(n):
        if (n == 0):
            return 1
        half = rec(n // 2)
        if (n % 2 == 0):
            return half * half % (10 ** 9 + 7)
        else:
            return half * half * 2 % (10 ** 9 + 7)

    return (rec(n) - 2) % (10 ** 9 + 7)

print(monkeyMove(0,n))