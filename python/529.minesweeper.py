class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        if board[x][y] != 'E':
            return board
        self.seen = {}
        return self.bfs(board, x, y)

    def bfs(self, board, x, y):
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        mine = 0
        # find the number of adjacent mines
        for dx, dy in steps:
            a, b = x + dx, y + dy
            if a >= 0 and b >= 0 and a < len(board) and b < len(board[0]) and board[a][b] == 'M':
                mine += 1

        # if the current grid is blank, the bfs its adjacent grid
        self.seen[x, y] = None
        if mine > 0:
            board[x][y] = str(mine)
        else:
            board[x][y] = 'B'
            for dx, dy in steps:
                a, b = x + dx, y + dy
                if (a, b) in self.seen:
                    continue
                if a >= 0 and b >= 0 and a < len(board) and b < len(board[0]):
                    board = self.bfs(board, a, b)
        return board
