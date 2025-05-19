n = 3
k = 1

def findKthBit(self, n: int, k: int) -> str:
    def rec(n, k):
        if (n == 1):
            return 0
        if (k < 2 ** (n - 1)):
            return rec(n - 1, k)
        elif (k > 2 ** (n - 1)):
            return 1 - (rec(n - 1, (2 ** n - k)))
        elif (k == 2 ** (n - 1)):
            return 1

    return str(rec(n, k))

print(findKthBit(0,n,k))