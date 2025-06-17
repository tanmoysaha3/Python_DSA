#TLE
def climbStairsTLE(self, n: int) -> int:
    res=[0]
    def rec(z):
        if(z==n):
            res[0]+=1
            return
        if(z>n):
            return
        rec(z+1)
        rec(z + 2)
    rec(0)
    return res[0]

#print(climbStairsTLE(0,45))


# Same as Fibonacci
# Recursion - TLE - Though better than before
def climbStairsTLE2(self, n: int) -> int:
    def rec(n):
        if (n <= 3):
            return n
        else:
            return rec(n - 1) + rec(n - 2)
    return rec(n)

#print(climbStairsTLE2(0,45))


# Own version of recursion
def climbStairsOv(self, n: int) -> int:
    if(n<=3):
        return n
    def rec(x,y,z):
        if(z==n):
            return y
        return rec(y,x+y,z+1)
    return rec(1,2,1)

#print(climbStairsOv(0,30))


# DP - Memorization
def climbStairsM(self, n: int) -> int:
    dp={1:1, 2:2}
    def dyPro(n):
        if(n not in dp):
            dp[n]=dyPro(n-1)+dyPro(n-2)
        return dp[n]
    return dyPro(n)

print(climbStairsM(0,45))


# Tabulation
def climbStairsT(self, n: int) -> int:
    dp=[1]*(n)
    if(n>1):
        dp[1]=2
    cout=2
    while(cout<n):
        dp[cout]=dp[cout-1]+dp[cout-2]
        cout+=1
    return dp[n-1]

print(climbStairsT(0,45))


# Space Optimized Tabulation
def climbStairsSoT(self, n: int) -> int:
    if(n<=3):
        return n
    prev=1
    curr=2
    cout=2
    while(cout<n):
        nxt=prev+curr
        prev=curr
        curr=nxt
        cout+=1
    return curr

print(climbStairsSoT(0,45))


# Space Optimized Tabulation - Less space
def climbStairsSoT2(self, n: int) -> int:
    if(n<=3):
        return n
    prev=1
    curr=2
    cout=2
    while(cout<n):
        prev, curr = curr, prev+curr
        cout+=1
    return curr

print(climbStairsSoT2(0,45))


# Space Optimized Tabulation - Using Function
def climbStairsSoTF(self, n: int) -> int:
    if(n<=3):
        return n
    def dyPro(prev,curr,cout):
        if(cout==n):
            return curr
        return dyPro(curr,prev+curr,cout+1)
    return dyPro(2,3,3)

print(climbStairsSoTF(0,45))
