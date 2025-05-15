#Try to draw Recursion Tree (up to down)
# and solve last 3/4 steps to get the pattern or logic or rule of return
#Recursion Tree
#          f(5)          =  f(n)
#          f(4)*5        =  f(n-1) * n
#          f(3)*4*5      =  f(n-2) * n-1 * n
#          f(2)*3*4*5    =  f(n-3) * n-2 * n-1 * n
#          f(1)*2*3*4*5  =  1*2*3*4*5
#Also see 509

n=5

def facto(n):
    def rec(n):
        if(n==1):
            return 1
        return rec(n-1)*n
    return rec(n)

print(facto(n))