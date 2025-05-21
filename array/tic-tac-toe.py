class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n  # Tracks sum of moves for each row
        self.cols = [0] * n  # Tracks sum of moves for each column
        self.diagonal = 0   # Tracks sum of moves on main diagonal (row == col)
        self.anti_diagonal = 0  # Tracks sum of moves on anti-diagonal (row + col == n-1)

    def move(self, row, col, player):

        value = 1 if player == 1 else -1

        self.rows[row] += value
        self.cols[col] += value

        if row == col:
            self.diagonal += value

        if row + col == self.n - 1:
            self.anti_diagonal += value

        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.anti_diagonal) == self.n):
            return player  # Return 1 for Player 1, 2 for Player 2

        return 0  # No win
