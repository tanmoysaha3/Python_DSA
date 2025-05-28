from typing import List


def solveNQueens(self, n: int) -> List[List[str]]:
    res=[]
    board=[['.']*n for _ in range(n)]
    def isValid(row, col, board):
        for i in range(row):
            if(board[i][col]=='Q'):
                return False
        for r,c in zip(range(row,-1,-1), range(col,-1,-1)):
            if(board[r][c]=='Q'):
                return False
        for r,c in zip(range(row,-1,-1), range(col,n)):
            if(board[r][c]=='Q'):
                return False
        return True

    def backT(board,row):
        if(row==n):
            res.append(["".join(row) for row in board])
            return
        for col in range(n):
            if(isValid(row,col, board)):
                board[row][col]="Q"
                backT(board, row+1)
                board[row][col]='.'

    backT(board,0)
    return res

n = 4
print(solveNQueens(0,n))