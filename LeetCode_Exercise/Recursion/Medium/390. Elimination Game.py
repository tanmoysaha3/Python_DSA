n=10**9

def lastRemaining(self, n: int) -> int:
    def rec(m, i, k):
        if(i+(2**k)>n):
            return i
        if(k%2==0):
            return rec(m//2, i+(2**k), k+1)
        else:
            if(m%2==0):
                return rec(m // 2, i, k + 1)
            else:
                return rec(m//2, i+(2**k), k+1)
    return rec(n,1,0)

print(lastRemaining(0,n))