n = 6
k = 5
#Normal
def findTheWinner1(self, n: int, k: int) -> int:
    x=[]
    for i in range(n):
        x.append(i+1)

    def rec(x,y):
        if(len(x)==1):
            return x[0]
        z=(y+k-1)%len(x)
        del x[z]
        return rec(x,z)
    return rec(x,0)
print(findTheWinner1(0,n,k))


#Recursion
def findTheWinner2(self, n: int, k: int) -> int:
    def rec(n):
        if (n == 1):
            return 0
        return (rec(n - 1) + k) % n

    return rec(n) + 1
print(findTheWinner2(0,n,k))


#Iteration
def findTheWinner3(self, n: int, k: int) -> int:
    x = 0
    for i in range(2, n + 1):
        x = (x + k) % i
    return x + 1
print(findTheWinner3(0,n,k))