#nums = [2,3,[4,1,2]]
#nums = [1,2,[7,[3,4],2]]
nums = [1,2,[3,4],[[2]]]

def powerSum(nums):
    def rec(degree, nums):
        y=0
        for i in nums:
            if(type(i)==list):
                y+=rec(degree+1, i)
            else:
                y+=i
        return y**degree
    return rec(1, nums)

print(powerSum(nums))