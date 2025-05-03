class TicTacToe {
private:
    vector<int> rows; // Tracks sum of moves for each row
    vector<int> cols; // Tracks sum of moves for each column
    int diagonal;     // Tracks sum of moves on main diagonal (row == col)
    int antiDiagonal; // Tracks sum of moves on anti-diagonal (row + col == n-1)
    int n;            // Board size

public:
    TicTacToe(int n) {
        this->n = n;
        rows.resize(n, 0);
        cols.resize(n, 0);
        diagonal = 0;
        antiDiagonal = 0;
    }
    
    int move(int row, int col, int player) {
        // Assign value: +1 for Player 1, -1 for Player 2
        int value = (player == 1) ? 1 : -1;
        
        // Update row and column sums
        rows[row] += value;
        cols[col] += value;
        
        // Update diagonal if move is on it (row == col)
        if (row == col) {
            diagonal += value;
        }
        
        // Update anti-diagonal if move is on it (row + col == n-1)
        if (row + col == n - 1) {
            antiDiagonal += value;
        }
        
        // Check for win: sum == +n (Player 1) or -n (Player 2)
        if (abs(rows[row]) == n || abs(cols[col]) == n || 
            abs(diagonal) == n || abs(antiDiagonal) == n) {
            return player; // Return 1 for Player 1, 2 for Player 2
        }
        
        return 0; // No win
    }
};