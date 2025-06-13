class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n  # Tracks sum of moves for each row
        self.cols = [0] * n  # Tracks sum of moves for each column
        self.diagonal = 0   # Tracks sum of moves on main diagonal (row == col)
        self.anti_diagonal = 0  # Tracks sum of moves on anti-diagonal (row + col == n-1)

    def move(self, row, col, player):

        player = 1 if player == 1 else -1

        self.rows[row] += player
        self.cols[col] += player

        if row == col:
            self.diagonal += player

        if row + col == self.n - 1:
            self.anti_diagonal += player

        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.anti_diagonal) == self.n):
            return player

        return 0  # No win

obj = TicTacToe(3)
print(obj.move(0, 0, 1))  # Player 1 moves at (0, 0)
print(obj.move(0, 2, 2))  # Player 2 moves at (0, 2)
print(obj.move(2, 2, 1))  # Player 1 moves at (2, 2)
print(obj.move(1, 1, 2))  # Player 2 moves at (1, 1)
print(obj.move(2, 0, 1))  # Player 1 moves at (2, 0)
print(obj.move(1, 0, 2))  # Player 2 moves at (1, 0)
print(obj.move(2, 1, 1))  # Player 1 moves at (1, 2) - Player 1 wins


# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves):

        row = [0] * 3
        cols = [0] * 3
        digonal = 0
        anitdigonal = 0

        for i, (r, c) in enumerate(moves):

            player = 1 if i % 2 == 0 else -1

            row[r] += player
            cols[c] += player

            if r == c:
                digonal += player

            if r + c == 2:
                anitdigonal += player

            if abs(row[r]) == 3 or abs(cols[c]) == 3 or abs(digonal) == 3 or abs(anitdigonal) == 3:
                return "A" if player == 1 else "B"

        return "Draw" if len(moves) == 9 else "Pending"
    
print(Solution().tictactoe([[0,0],[1,1],[0,1],[1,2],[0,2]]))  # "A"
print(Solution().tictactoe([[0,0],[1,1],[2,2],[0,1],[1,0],[2,1],[0,2]]))  # "B"