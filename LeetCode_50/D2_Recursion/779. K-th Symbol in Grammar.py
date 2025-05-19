#Try to think from up to down as tree - see 000

#Input
n=30
k=233192528

def kthGrammar(n, k):
    def rec(n, k):
        if (n == 1):
            return 0
        if (k <= pow(2, n - 2)):
            return rec(n - 1, k)
        else:
            k = k - pow(2, n - 2)
            return 1 - rec(n - 1, k)

    return rec(n, k)

print(kthGrammar(n, k))