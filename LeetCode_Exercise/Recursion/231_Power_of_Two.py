#input
n = 1

#Normal
import math
def isPowerOfTwo1(n):
    if (n < 1):
        return False
    elif (math.log2(n).is_integer()):
        return True
    else:
        return False


#Recursion
def isPowerOfTwo2(n):
    def rec(x):
        if(pow(2,x)>n):
            return False
        elif(pow(2,x)==n):
            return True
        return rec(x+1)
    return rec(0)

print(isPowerOfTwo1(n))
print(isPowerOfTwo2(n))