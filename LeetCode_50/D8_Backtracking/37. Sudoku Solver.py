import time
from typing import List

#New way
def solveSudoku1(self, board: List[List[str]]) -> None:
    s = {str(i) for i in range(1, 10)}
    x = [set() for i in range(9)]
    y = [set() for i in range(9)]
    z = [set() for i in range(9)]
    for row in range(9):
        for col in range(9):
            a = board[row][col]
            if (a.isdigit()):
                x[row].add(a)
                y[col].add(a)
                z[(row // 3) * 3 + col // 3].add(a)

    c = dict()
    for row in range(9):
        for col in range(9):
            if (board[row][col] == '.'):
                c[str(row) + str(col)] = len(s - x[row] - y[col] - z[(row // 3) * 3 + col // 3])

    q = list(sorted(c, key=c.get))
    def fillBoard(board):
        b[0]+=1
        for i in q:
            row, col = int(i[0]), int(i[1])
            if(board[row][col]=='.'):
                a=s-x[row]-y[col]-z[(row//3)*3+col//3]
                for num in a:
                    board[row][col]=num
                    x[row].add(num)
                    y[col].add(num)
                    z[(row//3)*3+col//3].add(num)
                    if(fillBoard(board)):
                        return True
                    board[row][col]='.'
                    x[row].remove(num)
                    y[col].remove(num)
                    z[(row // 3) * 3 + col // 3].remove(num)
                return False
        return True

    fillBoard(board)


#Dont work anymore TLE
def solveSudoku2(self, board: List[List[str]]) -> None:
    def isValid(num, row, col):
        b[1]+=1
        for i in range(9):
            if((board[i][col]==num) or(board[row][i]==num)):
                return False
            r=3*(row//3)+i//3
            c=3*(col//3)+i%3
            if(board[r][c]==num):
                return False
        return True
    def fillBoard(board):
        for row in range(9):
            for col in range(9):
                if(board[row][col]=='.'):
                    for num in '123456789':
                        if(isValid(num, row, col)):
                            board[row][col]=num
                            if(fillBoard(board)):
                                return True
                            board[row][col]='.'
                    return False
        return True

    fillBoard(board)

b=[0,0]
board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
start1 = time.perf_counter()
solveSudoku1(0,board)
end1 = time.perf_counter()
print(b[0]," Runtime:", end1 - start1, "seconds")
board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
start2 = time.perf_counter()
solveSudoku2(0,board)
end2 = time.perf_counter()
print(board)
print(b[1]," Runtime:", end2 - start2, "seconds")