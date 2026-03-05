'''
Explain low level design for 2 player chess game, assume both players are human, the app is just providing a platform to the players.

requirements:

1. will need player class, to represent the players containing details like: name, color.

2. Interface for piece, which all pieces( knight, king,.. ) will extend and implement valid move function, which based on piece's constraint return true or false.

3. Cell class for defining ech cell of grid board. Holding properties like x, y coordinate, color, currently occupied or not. If occupied then piece on cell.

4. Game class, having a 2D matrix of type grid, 2 Players. The constructor will initilize the game.
    . Functions to be exposed to UI are in this call.. and should internally call the functions of piece, grid & player.

'''


from enum import Enum
from abc import ABC, abstractmethod

# --- Enums ---
class State(Enum):
    ACTIVE = 1
    PLAYING = 2
    WHITEWON = 3
    BLACKWON = 4

class Color(Enum):
    WHITE = 1
    BLACK = 2

# --- Piece Logic ---
class Piece(ABC):
    def __init__(self, p_x: int, p_y: int, color: Color):
        self.position_x = p_x
        self.position_y = p_y
        self.color = color

    def set_x(self, x: int):
        self.position_x = x

    def set_y(self, y: int):
        self.position_y = y

    @abstractmethod
    def can_move(self, next_x: int, next_y: int) -> bool:
        pass

class King(Piece):
    def can_move(self, next_x, next_y):
        return not (next_x == self.position_x and next_y == self.position_y)

class Knight(Piece):
    def can_move(self, next_x, next_y):
        return not (next_x == self.position_x and next_y == self.position_y)

class Queen(Piece):
    def can_move(self, next_x, next_y):
        return not (next_x == self.position_x and next_y == self.position_y)

class Rook(Piece):
    def can_move(self, next_x, next_y):
        return not (next_x == self.position_x and next_y == self.position_y)

class Pawn(Piece):
    def can_move(self, next_x, next_y):
        return not (next_x == self.position_x and next_y == self.position_y)

# --- Player Logic ---
class Player:
    def __init__(self, name: str, color: Color):
        self.name = name
        self.color = color

class WhitePlayer(Player):
    def __init__(self, name: str):
        super().__init__(name, Color.WHITE)

class BlackPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name, Color.BLACK)

# --- Game Engine ---
class Game:
    def __init__(self):
        # Initialize 8x8 board with None
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.state = State.ACTIVE
        self.player_turn = Color.WHITE  # Starting with White
        self.history = []
        self._init_game()

    def _turn(self):
        self.player_turn = Color.BLACK if self.player_turn == Color.WHITE else Color.WHITE

    def _init_game(self):
        # Placing pieces InitGame
        self.board[0][0] = Rook(0, 0, Color.WHITE)
        self.board[0][1] = Queen(0, 1, Color.WHITE)
        self.board[0][2] = Pawn(0, 2, Color.WHITE)
        self.board[2][3] = Knight(2, 3, Color.BLACK)
        self.board[3][5] = Rook(3, 5, Color.BLACK)

    def move(self, player: Player, start_x: int, start_y: int, end_x: int, end_y: int):
        if self.player_turn != player.color:
            raise Exception(f"It is not {player.name}'s turn")

        piece = self.board[start_x][start_y]
        if piece is None:
            raise Exception("No piece at starting position")

        if piece.can_move(end_x, end_y):
            self._make_move(piece, start_x, start_y, end_x, end_y)
            self._check_winner()
            print(f"Moved {type(piece).__name__} to {end_x},{end_y}")
            return

        raise Exception("Choose correct position to move")

    def _make_move(self, p: Piece, s_x, s_y, e_x, e_y):
        p.set_x(e_x)
        p.set_y(e_y)
        self.board[e_x][e_y] = p
        self.board[s_x][s_y] = None # Clear old position
        self.history.append(p)
        self._turn()

    def _check_winner(self):
        # TODO: scan whole board to find winner and change state
        pass

    def get_state(self):
        return self.state

    def get_winner(self):
        if self.state not in [State.WHITEWON, State.BLACKWON]:
            raise Exception("Game not finished or started")
        return Color.WHITE if self.state == State.WHITEWON else Color.BLACK

if __name__ == "__main__":
    game = Game()

    white_p = WhitePlayer("Mark")
    black_p = BlackPlayer("Steve")

    try:
        # Note: In your InitGame, 1,1 is empty, 
        # but following your main method logic:
        game.move(white_p, 0, 0, 0, 5) 
        game.move(black_p, 2, 3, 4, 4)
    except Exception as e:
        print(f"Error: {e}")