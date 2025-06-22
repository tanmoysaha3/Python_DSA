# Tabulation
def countHousePlacementsT(self, n: int) -> int:
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=2
    cout=2
    while(cout<=n):
        dp[cout]=dp[cout-1]+dp[cout-2]
        cout+=1
    return (dp[n]**2)%(10**9+7)

print(countHousePlacementsT(0,4))


# Space Optimized Tabulation
def countHousePlacementsSoT(self, n: int) -> int:
    prev=1
    curr=2
    cout=2
    while(cout<=n):
        prev,curr=curr,prev+curr
        cout+=1
    return (curr**2)%(10**9+7)

print(countHousePlacementsSoT(0,4))
