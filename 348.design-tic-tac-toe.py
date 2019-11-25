class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = {i: [] for i in range(n)}
        self.cols = {i: [] for i in range(n)}
        self.diag = {'lurd': [], 'ldru': []}
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        competitor = 1 if player == 2 else 2
        if row in self.rows:
            if competitor in self.rows[row]:
                del self.rows[row]
            else:
                self.rows[row].append(player)
                if len(self.rows[row]) == self.n:   return player
        if col in self.cols:
            if competitor in self.cols[col]:
                del self.cols[col]
            else:
                self.cols[col].append(player)
                if len(self.cols[col]) == self.n:   return player
        if row == col and 'lurd' in self.diag:
            if competitor in self.diag['lurd']:
                del self.diag['lurd']
            else:
                self.diag['lurd'].append(player)
                if len(self.diag['lurd']) == self.n: return player
        if row + col == self.n - 1 and 'ldru' in self.diag:
            if competitor in self.diag['ldru']:
                del self.diag['ldru']
            else:
                self.diag['ldru'].append(player)
                if len(self.diag['ldru']) == self.n: return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)