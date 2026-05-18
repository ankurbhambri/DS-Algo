# https://leetcode.com/problems/range-sum-query-2d-mutable/


class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return
        
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        
        # Build the tree using clear for loops
        for r in range(self.m):
            for c in range(self.n):
                self.update(r, c, matrix[r][c])

    def _get_update_indices(self, start: int, limit: int):
        """Generates indices for the update path using a generator."""
        curr = start + 1
        while curr <= limit:
            yield curr
            curr += curr & -1 * curr

    def _get_query_indices(self, start: int):
        """Generates indices for the query path using a generator."""
        curr = start + 1
        while curr > 0:
            yield curr
            curr -= curr & -1 * curr

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        # Clean, readable nested FOR loops
        for i in self._get_update_indices(row, self.m):
            for j in self._get_update_indices(col, self.n):
                self.tree[i][j] += delta

    def _query(self, row: int, col: int) -> int:
        total = 0
        # Clean, readable nested FOR loops
        for i in self._get_query_indices(row):
            for j in self._get_query_indices(col):
                total += self.tree[i][j]
        return total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._query(row2, col2) 
            - self._query(row1 - 1, col2) 
            - self._query(row2, col1 - 1) 
            + self._query(row1 - 1, col1 - 1)
        )