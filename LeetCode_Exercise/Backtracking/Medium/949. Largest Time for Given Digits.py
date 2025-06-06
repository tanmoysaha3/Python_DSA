from typing import List


def largestTimeFromDigits(self, arr: List[int]) -> str:
    n = len(arr)
    res = [""]

    def backT(index):
        if (index == n - 1):
            z = [str(arr[0]) + str(arr[1]), str(arr[2]) + str(arr[3])]
            if (z[0] <= "23" and z[1] <= "59"):
                res.append(z[0] + ':' + z[1])
            return
        for j in range(index, n):
            arr[index], arr[j] = arr[j], arr[index]
            backT(index + 1)
            arr[index], arr[j] = arr[j], arr[index]

    backT(0)
    return max(res)
arr = [5,5,5,5]
print(largestTimeFromDigits(0,arr))