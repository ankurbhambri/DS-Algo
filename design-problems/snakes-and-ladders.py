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
