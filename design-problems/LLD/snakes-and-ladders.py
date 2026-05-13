# https://leetcode.com/problems/snakes-and-ladders

from collections import deque

# Breadth-First Search (BFS)
class Solution:
    def snakesAndLadders(self, board):

        length = len(board)
        board.reverse()

        q = deque() 
        q.append([1, 0]) # [square, moves]
        visit = set()

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2 != 0:
                c = length - 1 - c
            return [r, c]

        while q:

            square, moves = q.popleft()
            for i in range(1, 7): 

                nextSquare = square + i

                r, c = intToPos(nextSquare)

                if board[r][c] != -1:
                    print(r, c)
                    nextSquare = board[r][c]

                if nextSquare == length * length:
                    return moves + 1

                if nextSquare not in visit:
                    q.append([nextSquare, moves + 1])
                    visit.add(nextSquare)

        return -1


print(Solution().snakesAndLadders(
    [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
    ]
))  # Output: 4
print(Solution().snakesAndLadders(
    [
        [-1,-1],
        [-1,3]
    ]
))  # Output: 1



'''
Design Snake and Ladder

Functional Requirements
    Multiple players (2-6)
    Board with fixed size (usually 100 cells)
    Dice roll (1-6)
    Snakes move player down
    Ladders move player up
    Player must land exactly on the last cell to win
    Turn-based gameplay
    Game ends when one player wins

Non-Functional Requirements
    Deterministic and fair gameplay
    Fast response (real-time turns)
    Easy to extend (online multiplayer, bots)
    Thread-safe for concurrent users

Note: Always confirm rules like “exact 100” and “extra turn on 6”. It shows attention to detail.

'''

import random
from collections import deque

class Jump:
    """Represents either a Snake or a Ladder."""
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Board:
    def __init__(self, size: int):
        self.size = size
        self.jumps = {}  # Map of start_pos -> Jump object

    def add_jump(self, start: int, end: int):
        self.jumps[start] = Jump(start, end)

    def get_final_position(self, pos: int) -> int:
        if pos in self.jumps:
            jump = self.jumps[pos]
            type_str = "Ladder" if jump.end > jump.start else "Snake"
            print(f"  -- Encountered a {type_str}! Moving {jump.start} -> {jump.end}")
            return jump.end
        return pos

class Player:
    def __init__(self, name: int):
        self.name = name
        self.position = 0

class Dice:
    def __init__(self, count: int = 1):
        self.count = count

    def roll(self) -> int:
        return sum(random.randint(1, 6) for _ in range(self.count))

class Game:
    def __init__(self, board_size: int, player_names: list):
        self.board = Board(board_size)
        self.dice = Dice()
        self.players = deque([Player(name) for name in player_names])
        self.winner = None

    def setup_default_jumps(self):
        # Ladders
        self.board.add_jump(2, 38); self.board.add_jump(4, 14)
        self.board.add_jump(9, 31); self.board.add_jump(33, 85)
        # Snakes
        self.board.add_jump(17, 7); self.board.add_jump(54, 34)
        self.board.add_jump(62, 19); self.board.add_jump(98, 79)

    def start_game(self):
        print(f"--- Game Started with {len(self.players)} players ---")
        
        while not self.winner:
            current_player = self.players.popleft()
            roll = self.dice.roll()
            print(f"{current_player.name} rolled a {roll}")

            initial_pos = current_player.position
            next_pos = initial_pos + roll

            # Rule: Exact 100 to win
            if next_pos > self.board.size:
                print(f"  {current_player.name} needs exact roll to finish. Staying at {initial_pos}")
            else:
                # Rule: Apply Snakes/Ladders
                next_pos = self.board.get_final_position(next_pos)
                current_player.position = next_pos
                print(f"  {current_player.name} moved {initial_pos} -> {next_pos}")

            # Check Win Condition
            if current_player.position == self.board.size:
                self.winner = current_player
                print(f"\n*** {current_player.name} WINS THE GAME! ***")
                break
            
            # Rule: Extra turn on 6
            if roll == 6:
                print(f"  {current_player.name} rolled a 6! Extra turn.")
                self.players.appendleft(current_player)
            else:
                self.players.append(current_player)

# --- Execution ---
if __name__ == "__main__":
    game = Game(board_size=100, player_names=["Alice", "Bob", "Charlie"])
    game.setup_default_jumps()
    game.start_game()