from collections import Counter
from itertools import chain
from typing import List


def exist1(self, board: List[List[str]], word: str) -> bool:
    a,b,c = len(board), len(board[0]), len(word)

    def backT(i,j,k):
        if(board[i][j]!=word[k]):
            return False
        if (k + 1 == c):
            return True
        board[i][j]='@'
        for m,n in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
            if(m>=0 and n>=0 and m<a and n<b):
                if(backT(m, n, k + 1)):
                    return True
        board[i][j] = word[k]
        return False

    for i in range(a):
        for j in range(b):
            if(backT(i,j,0)):
                return True

    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist1(0,board,word))

#Slight Optimization
def exist2(self, board: List[List[str]], word: str) -> bool:
    a, b, c = len(board), len(board[0]), len(word)
    if (c > a * b):
        return False

    if (not (Counter(word)) <= Counter(chain(*board))):
        return False

    def backT(i, j, k):
        if (board[i][j] != word[k]):
            return False
        if (k + 1 == c):
            return True
        board[i][j] = '@'
        for m, n in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if (m >= 0 and n >= 0 and m < a and n < b):
                if (backT(m, n, k + 1)):
                    return True
        board[i][j] = word[k]
        return False

    for i in range(a):
        for j in range(b):
            if (backT(i, j, 0)):
                return True

    return False
