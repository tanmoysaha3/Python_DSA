n = 7

#Normal
def fib1(n):
    x = [0, 1]
    if (n == 0):
        return 0
    for i in range(2, n):
        x.append(x[-1] + x[-2])
    return sum(x[-2:])


#Recursion - bottom to top
def fib2(n):
    if (n == 0):
        return 0
    def rec(x, y, z):
        if (z == n):
            return y
        return rec(y, x+y, z+1)
    return rec(0, 1, 1)


print(fib1(n))
print(fib2(n))