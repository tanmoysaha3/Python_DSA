#Fibinacci
def fib(n):
    def rec(x,y,z):
        if(z==n):
            return y
        return rec(y,x+y,z+1)
    return rec(0,1,1)

print(fib(0))