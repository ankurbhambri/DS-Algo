'''
Othello is played as follows: Each Othello piece is white on one side and
black on the other. When a piece is surrounded by its opponents on both
the left and right sides, or both the top and bottom, it is said to be captured
and its color is flipped. On your turn, you must capture at least one of your
opponent's pieces. The game ends when either user has no more valid
moves. The win is assigned to the person with the most pieces. Implement
the object-oriented design for Othello.
'''

from enum import Enum

class Color(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    def flip(self):
        if self == Color.BLACK: return Color.WHITE
        if self == Color.WHITE: return Color.BLACK
        return Color.EMPTY


class Piece:
    def __init__(self, color):
        self.color = color

    def flip(self):
        self.color = self.color.flip()


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_center()

    def initialize_center(self):
        # Othello starts with 4 pieces in the center
        self.grid[3][3] = Piece(Color.WHITE)
        self.grid[3][4] = Piece(Color.BLACK)
        self.grid[4][3] = Piece(Color.BLACK)
        self.grid[4][4] = Piece(Color.WHITE)

    def place_piece(self, row, col, color):
        # 1. Place the new piece
        self.grid[row][col] = Piece(color)
        # 2. Flip captured pieces in all 8 directions
        self.flip_captured_pieces(row, col, color)

    def flip_captured_pieces(self, row, col, color):
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        for dr, dc in directions:
            self._capture_in_direction(row, col, dr, dc, color)

    def _capture_in_direction(self, row, col, dr, dc, color):
        # Implementation of the "Sandwich" logic:
        # Travel in a direction to see if you hit your own color
        # and flip everything in between.
        r, c = row + dr, col + dc
        pieces_to_flip = []
        while 0 <= r < 8 and 0 <= c < 8:
            piece = self.grid[r][c]
            if piece is None:
                return  # No pieces to flip in this direction
            if piece.color == color:
                # Flip all pieces in pieces_to_flip
                for pr, pc in pieces_to_flip:
                    self.grid[pr][pc].flip()
                return
            else:
                pieces_to_flip.append((r, c))
            r += dr
            c += dc


class OthelloGame:
    def __init__(self):
        self.board = Board()
        self.turn = Color.BLACK # Black always goes first
    
    def play_move(self, row, col):
        if self.is_valid_move(row, col, self.turn):
            self.board.place_piece(row, col, self.turn)
            self.switch_turn()
        else:
            print("Invalid Move!")

    def is_valid_move(self, row, col, color):
        # Must be empty AND must capture at least one opponent piece
        if self.board.grid[row][col] is not None:
            return False
        # Logic to check if move surrounds any opponent pieces...
        return True

    def get_score(self):
        black_count = 0
        white_count = 0
        for row in self.board.grid:
            for piece in row:
                if piece:
                    if piece.color == Color.BLACK: black_count += 1
                    else: white_count += 1
        return black_count, white_count

    def check_game_over(self):
        if not self.has_valid_move(Color.BLACK) and not self.has_valid_move(Color.WHITE):
            b, w = self.get_score()
            if b > w:
                return "Game Over! Winner: Black"
            elif w > b:
                return "Game Over! Winner: White"
            else:
                return "Game Over! It's a tie!"
        return "Keep Playing"


    def has_valid_move(self, color):
        # Check if the player has any valid moves left
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col, color):
                    return True
        return False
    
    def switch_turn(self):
        self.turn = Color.BLACK if self.turn == Color.WHITE else Color.WHITE


game = OthelloGame()
game.play_move(2, 3) # Black moves
game.play_move(2, 2) # White moves
print(game.get_score())