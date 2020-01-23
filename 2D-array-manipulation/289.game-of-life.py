class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """    
        # 2 represent new live, prev dead
        # -1 represent new dead, prev live
        def search(x: int, y: int):
            steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            live, dead = 0, 0
            for dx, dy in steps:
                a, b = x+ dx, y + dy
                if a >= 0 and b >= 0 and a < len(board) and b < len(board[0]):
                    if board[a][b] == 1 or board[a][b] == -1:
                        live += 1
                    else:
                        dead += 1
            if board[x][y] == 1:
                if live > 3 or live < 2:
                    board[x][y] = -1
            else:
                if live == 3:
                    board[x][y] = 2

        for row in range(len(board)):
            for col in range(len(board[0])):
                search(row, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == -1:
                    board[row][col] = 0
