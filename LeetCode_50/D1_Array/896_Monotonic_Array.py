#input
nums = [1,2,2,3]

def isMonotonic1(nums):
    x = set()
    for i in range(1, len(nums)):
        if (nums[i - 1] < nums[i]):
            x.add(True)
        elif (nums[i - 1] > nums[i]):
            x.add(False)
        if (len(x) == 2):
            return False
    if (len(x) == 2):
        return False
    else:
        return True

#Or
def isMonotonic2(nums):
    x = len(nums)
    if (x > 1):
        if (nums[0] > nums[-1]):
            for i in range(x - 1):
                if (nums[i] < nums[i + 1]):
                    return False
        elif (nums[0] == nums[-1]):
            if (len(set(nums)) > 1):
                return False
        elif (nums[0] < nums[-1]):
            for i in range(x - 1):
                if (nums[i] > nums[i + 1]):
                    return False
        return True
    return True

print(isMonotonic1(nums))
print(isMonotonic2(nums))