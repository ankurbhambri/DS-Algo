# For prifix sum on grid 

- First thing we calculate a cummulative sum of the element of the grid, While building the prefix sum, we add the top and left values to include all sums up to the current cell. We subtract the diagonal (top-left) value to avoid double-counting the overlapping region.
- ex. prefix[i][j] = grid[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

- Second, For a given range, we reverse this logic. Starting with the bottom-right corner (which includes the total sum of all cells up to that point), we subtract the areas outside the desired range (top rows and left columns). Since the diagonal region gets subtracted twice, we add it back to correct the sum

- ex. Sum = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]

```
This ensures that :-

The top and left values are excluded from the result.
The diagonal is re-added to balance the double subtraction.
```