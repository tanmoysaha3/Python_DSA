# Recursion
def knapsack1(w,val,wt):
    x=[0]
    def rec(index, sw, total):
        if(index==len(val) or sw>w):
            if(total>x[0] and sw<=w):
                x[0]=total
            return
        rec(index+1, sw+wt[index], total+val[index])
        rec(index+1, sw, total)
    rec(0, 0, 0)
    return x[0]


def knapsack2(w,val,wt):
    x=[0]
    def rec(index, sw, total):
        if(index==len(val)):
            if(total>x[0]):
                x[0]=total
            return
        if(sw+wt[index]<=w):
            rec(index+1, sw+wt[index], total+val[index])
        rec(index+1, sw, total)
    rec(0, 0, 0)
    return x[0]


def knapsack3(w,val,wt):
    x=[0]
    def rec(index, remainingWeight, total):
        if(index==len(val)):
            if(total>x[0]):
                x[0]=total
            return
        if(wt[index]<=remainingWeight):
            rec(index+1, remainingWeight-wt[index], total+val[index])
        rec(index+1, remainingWeight, total)
    rec(0, w, 0)
    return x[0]

def knapsackR(w,val,wt):
    def rec(index, remainingWeight):
        if(index==len(val) or remainingWeight==0):
            return 0
        inclu = 0
        if(wt[index]<=remainingWeight):
             inclu = val[index] + rec(index+1, remainingWeight-wt[index])
        exclu = rec(index+1, remainingWeight)
        return max(inclu, exclu)
    return rec(0, w)

def knapsackM(w,val,wt):
    dp = [[-1]*(w+1) for i in range(len(val))]
    def rec(index, remainingWeight):
        if(index==len(val) or remainingWeight==0):
            return 0
        if(dp[index][remainingWeight]!=-1):
            return dp[index][remainingWeight]
        inclu = 0
        if(wt[index]<=remainingWeight):
             inclu = val[index] + rec(index+1, remainingWeight-wt[index])
        exclu = rec(index+1, remainingWeight)
        dp[index][remainingWeight] = max(inclu, exclu)
        return dp[index][remainingWeight]
    return rec(0, w)

def knapsackT(w, val, wt):
    dp = [[0]*(w+1) for i in range(len(val)+1)]

    for i in range(1,len(val)+1):
        for j in range(1, w + 1):
            exclude=dp[i-1][j]
            include=0
            if(wt[i-1]<=j):
                include=val[i-1]+dp[i-1][j-wt[i-1]]
            dp[i][j]=max(include, exclude)
    return dp[len(val)][w]

def knapsackSoT(w, val, wt):
    prev = [0]*(w+1)
    curr = [0] * (w + 1)

    for i in range(1,len(val)+1):
        for j in range(1, w + 1):
            exclude=prev[j]
            include=0
            if(wt[i-1]<=j):
                include=val[i-1]+prev[j-wt[i-1]]
            curr[j]=max(include, exclude)
        prev[:]=curr[:]
    return curr[w]


W = 4
val = [1, 2, 3]
wt = [4, 5, 1]
#print(knapsack1(W,val,wt))
#print(knapsack2(W,val,wt))
#print(knapsack3(W,val,wt))

print(knapsackR(W,val,wt))
print(knapsackM(W,val,wt))
print(knapsackT(W,val,wt))
