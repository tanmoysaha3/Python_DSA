from typing import List


def letterCasePermutation(self, s: str) -> List[str]:
    x = len(s)
    res = []

    def backT(index, subset):
        if (index == x):
            res.append(subset)
            return
        if (s[index].isalpha()):
            backT(index + 1, subset + s[index].lower())
            backT(index + 1, subset + s[index].upper())
        else:
            i = 0
            while (index + i < x and s[index + i].isdigit()):
                i += 1
            # print(i, subset + [s[index:index+i]])
            backT(index + i, subset + s[index:index + i])

    backT(0, "")
    return res


s = "a122b2"
print(letterCasePermutation(0, s))
