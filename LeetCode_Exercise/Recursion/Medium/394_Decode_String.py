#s = "3[a2[c]]"
s = "3[a]2[bc]"


import re

# No recursion
def decodeString1(self, s: str) -> str:
    pattern = r'(\d+)\[([a-z]+)\]'
    while True:
        match = re.search(pattern, s)
        if not match:
            return s

        number = match.group(1)
        chars = match.group(2)

        replacement = int(match.group(1)) * match.group(2)
        start, end = match.span()
        s = s[:start] + replacement + s[end:]


# Using Recursion
def decodeString2(self, s: str) -> str:
    def rec(s):
        pattern = r'(\d+)\[([a-z]+)\]'
        if(re.search(pattern,s)==None):
            return s
        x=0
        for match in re.finditer(pattern, s):
            a=int(match.group(1))*match.group(2)
            s=s[:match.start()-x]+a+s[-x+match.end():]
            x+=len(match.group(0))-len(a)
        return rec(s)
    return rec(s)

print(decodeString1(0,s))
print(decodeString2(0,s))