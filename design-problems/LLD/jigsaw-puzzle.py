'''
Implement a jigsaw puzzle. Design the data structures and explain an
algorithm to solve the puzzle. You can assume that you have a fitsWith
method which, when passed two puzzle pieces (and the sides being matched),
returns true if those two edges belong together.

Design notes
------------
Data structures:
  - Edge:  enum describing the shape of one side of a piece
           (INNER tab, OUTER tab, or FLAT border).
  - Side:  enum naming the four sides of a piece (TOP/RIGHT/BOTTOM/LEFT)
           so we can talk about "the right edge of piece A meets the
           left edge of piece B".
  - Piece: holds an id and a dict {Side: Edge}. Supports rotate() which
           shifts the edges 90 degrees clockwise.
  - JigsawPuzzle: width x height board (2D list of Piece) plus the pool
           of unused pieces.

Algorithm (corner + edge expansion):
  1. Pick any corner piece (2 FLAT edges), rotate it so TOP and LEFT
     are FLAT, place at (0, 0).
  2. Walk the board row by row, left to right. For each empty cell:
       - figure out which sides must be FLAT (cell on the outer border)
         and which neighbours already exist (top / left).
       - search the remaining pool for a piece that, in some rotation,
         satisfies the border constraints and matches the neighbours
         using fitsWith on the touching edges.
       - place it and remove it from the pool.
  3. If no piece fits, the input is inconsistent.

Complexity: O(N^2) edge comparisons in the worst case (N = number of
pieces) since each empty cell scans the remaining pool and tries up to
4 rotations.
'''

from enum import Enum


class Edge(Enum):
    INNER = 0   # Inward tab
    OUTER = 1   # Outward tab
    FLAT = 2    # Straight edge (border of the puzzle)


class Side(Enum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3


class Piece:
    def __init__(self, pid, edges):
        # edges: {Side.TOP: Edge.X, Side.RIGHT: Edge.X, ...}
        self.id = pid
        self.edges = dict(edges)
        self.orientation = 0  # 0, 90, 180, 270 (clockwise)

    def rotate(self):
        """Rotate piece 90 degrees clockwise: TOP <- LEFT, RIGHT <- TOP, ..."""
        self.orientation = (self.orientation + 90) % 360
        self.edges = {
            Side.TOP:    self.edges[Side.LEFT],
            Side.RIGHT:  self.edges[Side.TOP],
            Side.BOTTOM: self.edges[Side.RIGHT],
            Side.LEFT:   self.edges[Side.BOTTOM],
        }

    def flat_count(self):
        return sum(1 for e in self.edges.values() if e == Edge.FLAT)


class JigsawPuzzle:
    def __init__(self, width, height, pieces=None):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
        self.remaining_pieces = list(pieces) if pieces else []


def fitsWith(piece1, side1, piece2, side2):
    """Provided primitive: do these two edges (one from each piece) mate?
    Two FLAT edges never mate; INNER mates with OUTER. Replace the body
    with the real shape-matching implementation."""
    e1, e2 = piece1.edges[side1], piece2.edges[side2]
    if e1 == Edge.FLAT or e2 == Edge.FLAT:
        return False
    return {e1, e2} == {Edge.INNER, Edge.OUTER}


def fits_at_position(r, c, piece, puzzle):
    """Check if piece (in its current orientation) fits at (r, c)."""
    # Outer-border sides must be FLAT; interior sides must NOT be FLAT.
    on_top    = (r == 0)
    on_bottom = (r == puzzle.height - 1)
    on_left   = (c == 0)
    on_right  = (c == puzzle.width - 1)

    if (piece.edges[Side.TOP]    == Edge.FLAT) != on_top:    return False
    if (piece.edges[Side.BOTTOM] == Edge.FLAT) != on_bottom: return False
    if (piece.edges[Side.LEFT]   == Edge.FLAT) != on_left:   return False
    if (piece.edges[Side.RIGHT]  == Edge.FLAT) != on_right:  return False

    # Match against already-placed neighbours.
    if r > 0:
        top = puzzle.board[r - 1][c]
        if top and not fitsWith(top, Side.BOTTOM, piece, Side.TOP):
            return False
    if c > 0:
        left = puzzle.board[r][c - 1]
        if left and not fitsWith(left, Side.RIGHT, piece, Side.LEFT):
            return False
    return True


def find_matching_piece(r, c, puzzle):
    """Find a piece (and rotation) that fits at (r, c). Removes it from pool."""
    for piece in puzzle.remaining_pieces:
        for _ in range(4):
            if fits_at_position(r, c, piece, puzzle):
                puzzle.remaining_pieces.remove(piece)
                return piece
            piece.rotate()
        # After 4 rotations the piece is back to its original orientation.
    return None


def solve_puzzle(puzzle):
    # 1. Pick a corner and rotate it so TOP and LEFT are FLAT.
    corner = next((p for p in puzzle.remaining_pieces if p.flat_count() == 2), None)
    if corner is None:
        return False
    for _ in range(4):
        if corner.edges[Side.TOP] == Edge.FLAT and corner.edges[Side.LEFT] == Edge.FLAT:
            break
        corner.rotate()
    puzzle.remaining_pieces.remove(corner)
    puzzle.board[0][0] = corner

    # 2. Fill the rest in row-major order.
    for r in range(puzzle.height):
        for c in range(puzzle.width):
            if puzzle.board[r][c] is not None:
                continue
            piece = find_matching_piece(r, c, puzzle)
            if piece is None:
                return False  # Unsolvable with the given pieces.
            puzzle.board[r][c] = piece
    return True


if __name__ == "__main__":
    # Smoke test: 1x1 "puzzle" with a single all-FLAT piece.
    only = Piece("solo", {s: Edge.FLAT for s in Side})
    pz = JigsawPuzzle(1, 1, [only])
    assert solve_puzzle(pz)
    assert pz.board[0][0] is only
    print("ok")
