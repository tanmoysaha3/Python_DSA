def unboundedKnapsackT(w,val,wt):
    dp = [[0]*(w+1) for i in range(len(wt)+1)]
    for i in range(1,len(wt)+1):
        for j in range(1,w+1):
            exclu=dp[i-1][j]
            inclu=0
            if(wt[i-1]<=j):
                inclu=val[i-1]+dp[i][j-wt[i-1]]
            dp[i][j]=max(inclu,exclu)
    return dp[len(wt)][w]

def unboundedKnapsackSoT(w,val,wt):
    prev=[0]*(w+1)
    curr=[0]*(w+1)
    for i in range(1, len(wt) + 1):
        for j in range(1, w + 1):
            exclu=prev[j]
            inclu=0
            if(wt[i-1]<=j):
                inclu=val[i-1]+curr[j-wt[i-1]]
            curr[j] = max(inclu, exclu)
        prev[:]=curr[:]
    return curr[w]

W = 8
val = [1, 16, 3]
wt = [4, 5, 1]
print(unboundedKnapsackT(W,val,wt))
print(unboundedKnapsackSoT(W,val,wt))