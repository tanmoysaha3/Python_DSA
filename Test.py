#Fibinacci
import math
def fib(n,k):
    x=[]
    for i in range(n):
        x.append(i+1)
    print(x)
    y=set(x)
    j=0
    m=""
    while(k>0):
        a=k//len(y)
        m+=str(x[a])
        del x[a]
        print(a,m)
        k-=a+1
    for i in x:
        m+=str(i)
    return m

print(fib(4,9))