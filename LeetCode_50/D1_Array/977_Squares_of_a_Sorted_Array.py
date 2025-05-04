#Input
nums = [-7,-3,2,3,11]


def sortedSquares(nums):
    x = []
    a = 0
    b = len(nums) - 1
    while (b >= a):
        if (abs(nums[b]) > abs(nums[a])):
            x.append(nums[b] ** 2)
            b -= 1
        else:
            x.append(nums[a] ** 2)
            a += 1
    return x[::-1]

print(sortedSquares(nums))
