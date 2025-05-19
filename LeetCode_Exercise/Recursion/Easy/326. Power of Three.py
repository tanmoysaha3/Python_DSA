#Input
n=243

def isPowerOfThree(n):
    def rec(x):
        y = pow(3, x)
        if (y > n):
            return False
        elif (y == n):
            return True
        # print(x)
        return rec(x + 1)

    return rec(0)

print(isPowerOfThree(n))