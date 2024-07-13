from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board=[]
        width = len(board[0])
        height = len(board)
        for i in range(height):
            row = [0] * width
            new_board.append(row)

        for i, row in enumerate(board):
            for j, e in enumerate(row):
                count = 0
                if i-1>=0:
                    count+=board[i-1][j]
                    if j-1>=0:
                        count+=board[i-1][j-1]
                    if j+1<width:
                        count+=board[i-1][j+1]
                
                if j-1>=0:
                    count+=board[i][j-1]
                if j+1<width:
                    count+=board[i][j+1]

                if i+1<height:
                    count+=board[i+1][j]
                    if j-1>=0:
                        count+=board[i+1][j-1]
                    if j+1<width:
                        count+=board[i+1][j+1]

                if count < 2 or count > 3:
                    new_board[i][j]=0
                elif count == 3:
                    new_board[i][j]=1
                elif count == 2:
                    new_board[i][j] = board[i][j]
            
        for i in range(height):
            for j in range(width):
                board[i][j] = new_board[i][j]

    def gameOfLifeFaster(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        width = len(board[0])
        height = len(board)
        directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        for i in range(height):
            for j in range(width):
                life=0
                for direction in directions:
                    x=i+direction[0]
                    y=j+direction[1]
                    if (x>-1 and x<height and y>-1 and y<width and abs(board[x][y]) == 1):
                        life+=1
                if life == 3 and board[i][j] == 0:
                    board[i][j] = 2
                if life>3 and board[i][j] == 1:
                    board[i][j] = -1
                if life < 2 and board[i][j]==1:
                    board[i][j] = -1
                    
        for i in range(height):
            for j in range(width):
                board[i][j]=1 if board[i][j]>0 else 0
