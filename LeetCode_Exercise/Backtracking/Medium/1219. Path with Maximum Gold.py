from typing import List


def getMaximumGold1(self, grid: List[List[int]]) -> int:
    res = [0]
    a, b = len(grid), len(grid[0])

    def backT(i, j, k):
        if (grid[i][j] == 0):
            if (k > res[0]):
                res[0] = k
            return

        x = grid[i][j]
        k += x
        grid[i][j] = 0

        for m, n in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if (m >= 0 and n >= 0 and m < a and n < b):
                backT(m, n, k)

        grid[i][j] = x
        if (k > res[0]):
            res[0] = k

    for i in range(a):
        for j in range(b):
            backT(i, j, 0)
    return res[0]

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print(getMaximumGold1(0,grid))


# Small shortcut
def getMaximumGold2(self, grid: List[List[int]]) -> int:
    res = [0]
    a, b = len(grid), len(grid[0])
    if (a == 1 and b == 1):
        return grid[0][0]

    def backT(i, j, k):
        if (grid[i][j] == 0):
            if (k > res[0]):
                res[0] = k
            return

        x = grid[i][j]
        k += x
        grid[i][j] = 0

        for m, n in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if (m >= 0 and n >= 0 and m < a and n < b):
                backT(m, n, k)

        grid[i][j] = x

    for i in range(a):
        for j in range(b):
            backT(i, j, 0)
    return res[0]

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print(getMaximumGold2(0,grid))