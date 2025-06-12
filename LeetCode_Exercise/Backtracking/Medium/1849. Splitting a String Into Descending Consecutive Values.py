def splitString(self, s: str) -> bool:
    n = len(s)

    def backT(index, subset, y, z):
        print("subset",index,subset)
        if (y > 1):
            if (subset[-2] - subset[-1] != 1):
                return
            elif (z == n):
                print("True1")
                return True
        for i in range(index, n):
            # print(s[index:i+1])
            x = s[index:i + 1]
            if (backT(i + 1, subset + [int(x)], y + 1, z + len(x))):
                return True
        return False

    return backT(0, [], 0, 0)

s = "4321"
print(splitString(0,s))