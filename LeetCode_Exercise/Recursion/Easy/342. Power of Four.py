#Input
n=16

#Normal
def isPowerOfFour1(n):
    i = 0
    value = False
    while (4 ** i <= n):
        c = 4 ** i
        if (c == n):
            value = True
        i += 1
    return value

#Recursion
def isPowerOfFour2(n):
    def rec(x):
        y = pow(4, x)
        if (y > n):
            return False
        elif (y == n):
            return True
        # print(x)
        return rec(x + 1)

    return rec(0)

print(isPowerOfFour1(n))
print(isPowerOfFour2(n))