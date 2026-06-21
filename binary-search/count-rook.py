'''

Given N x N chess board

N-1 rooks already stay on board so that no one hitting each other. more formally:
    - no row contains more than 1 rook
    - no column contains more than 1 rook

Place Nth rook, return the position i, j where to place it, but you dont know where current rooks are located.

We have a function countRooksInsideRectangle(a,b,c,d) that returns number of rooks within rectangle formed by horizontals a, b (a<=b) and verticals c, d (c<=d)

Example:

n = 3

countRooksInsideRectangle(2,3,1,3) -> 2

countRooksInsideRectangle(1,1,1,1) -> 0

answer: (1,1) (since board is 1-indexed)

'''

def countRook(a: int, b: int, c: int, d: int) -> int:
    return 0

# a means number of rows, b means number of columns, c and d are the coordinates of the rectangle we want to check for rooks.
class Solution:
    def findMissingAndRepeatedValues(self, n: int):
        
        # Find missing row
        l, r = 1, n
        
        while l < r:
            mid = (l + r) // 2

            # Check if the number of rooks in the rectangle from (1, 1) to (mid, n) is equal to mid
            if countRook(1, 1, mid, n) == mid:
                l = mid + 1
            else:
                r = mid
        
        missing_row = l
        
        # Find missing column
        l, r = 1, n
        
        while l < r:
            mid = (l + r) // 2
            # Check if the number of rooks in the rectangle from (1, 1) to (n, mid) is equal to mid
            if countRook(1, 1, n, mid) == mid:
                l = mid + 1
            else:
                r = mid

        missing_col = l

        return [missing_row, missing_col]