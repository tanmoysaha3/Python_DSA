def myPow(self, x: float, n: int) -> float:
    def rec(x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / rec(x, -n)
        half = rec(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    return rec(x, n)

print(myPow(0,2,10))
print(myPow(0,2,-10))

# This don't work as it work linearly
# x =-1,   n = 2147483647
# x = 2.00000,   n = -2147483648
# def myPow(self, x: float, n: int) -> float:
#     def rec(x, n):
#         if (n == 0):
#             return 1
#         if (n < 0):
#             return 1 / x * rec(x, n + 1)
#         elif (n > 0):
#             return x * rec(x, n - 1)
#
#     return rec(x, n)