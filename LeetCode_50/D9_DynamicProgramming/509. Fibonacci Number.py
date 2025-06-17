n = 10

# Recursive way
def fibR(n):
    if(n<=1):
        return n
    else:
        return fibR(n-1)+fibR(n-2)

print("Recursion ",fibR(n))


# DP - Memorization
d={0:0,1:1}
def fibM(n):
    if(n in d):
        return d[n]
    else:
        d[n] = fibM(n-1)+fibM(n-2)
        return d[n]

print("DP - Memorization ",fibM(n))


# DP - Memorization - Updated to easier understanding
def fibM1(n):
    if(n not in d):
        d[n] = fibM(n-1)+fibM(n-2)
    return d[n]

print("DP - Memorization - Updated ",fibM1(n))


# Tabulation
def fibT(n):
    dp=[0]*(n+1)
    if(n>0):
        dp[1]=1

    count=2
    while(count<=n):
        dp[count]=dp[count-1]+dp[count-2]
        count+=1

    return dp[n]

print("Tabulation ",fibT(n))


# Space Optimized Tabulation
def fibSoT(n):
    if(n<=1):
        return n
    prev=0
    curr=1
    cont=2
    while(cont<=n):
        nxt=prev+curr
        prev=curr
        curr=nxt
        cont+=1

    return curr

print("Space Optimized Tabulation ",fibSoT(n))


# Own version
def fibOv(n):
    if (n <= 1):
        return n
    def rec(x, y, z):
        if (z == n):
            return y
        return rec(y, x+y, z+1)
    return rec(0, 1, 1)

print("Own version ",fibOv(n))
