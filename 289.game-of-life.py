# class Solution:
#     def gameOfLife(self, board: List[List[int]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         lives = [1, -1]
#         deaths = [0, 2]
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 alive = 0
#                 if i > 0 and board[i-1][j] in lives:
#                     alive += 1
#                 if i < len(board) - 1 and board[i+1][j] in lives:
#                     alive += 1
#                 if j > 0 and board[i][j-1] in lives:
#                     alive += 1
#                 if j < len(board[0]) - 1 and board[i][j+1] in lives:
#                     alive += 1
                
#                 if i > 0 and j > 0 and board[i-1][j-1] in lives:
#                     alive += 1
#                 if i > 0 and j < len(board[0]) - 1 and board[i-1][j+1] in lives:
#                     alive += 1
#                 if j > 0 and i < len(board) - 1 and board[i+1][j-1] in lives:
#                     alive += 1
#                 if j < len(board[0]) - 1 and i < len(board) - 1 and board[i+1][j+1] in lives:
#                     alive += 1
                
#                 if alive > 3:
#                     board[i][j] = -1 if board[i][j] == 1 else 0
#                 elif alive == 3:
#                     board[i][j] = 2 if board[i][j] == 0 else 1
#                 elif alive < 2:
#                     board[i][j] = -1 if board[i][j] == 1 else 0
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == -1:
#                     board[i][j] = 0
#                 elif board[i][j] == 2:
#                     board[i][j] = 1

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lives = [1, -1]
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                alive = 0
                for neighbor in neighbors:
                    x = i + neighbor[0]
                    y = j + neighbor[1]
                    if 0 <= x and 0 <= y and x < len(board) and y < len(board[0]) and board[x][y] in lives:
                        alive += 1
                
                if alive > 3:
                    board[i][j] = -1 if board[i][j] == 1 else 0
                elif alive == 3:
                    board[i][j] = 2 if board[i][j] == 0 else 1
                elif alive < 2:
                    board[i][j] = -1 if board[i][j] == 1 else 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
