# Backtracling maybe too complex
def smallestNumber(self, pattern: str) -> str:
    res=[]
    lst=[i+1 for i in range(len(pattern)+1)]
    print(lst)
    def backT(index):
        if(index==len(pattern)):
            return
        if(pattern[index]=="D"):
            y=0
            while(y+index<len(pattern) and pattern[y+index]=='D'):
                y+=1
            res.append(str(lst[y]))
            del lst[y]
        else:
            res.append(str(lst[0]))
            del lst[0]
        backT(index+1)

    backT(0)
    res.append(str(lst[0]))
    return "".join(res)

pattern = "IIIDIDDD"
print(smallestNumber(0,pattern))