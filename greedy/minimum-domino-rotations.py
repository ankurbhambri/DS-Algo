# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row

def minDominoRotations(tops, bottoms):
    def check(x):
        rotations_top = rotations_bottom = 0
        for i in range(len(tops)):
            if tops[i] != x and bottoms[i] != x:
                return -1
            elif tops[i] != x:
                rotations_top += 1
            elif bottoms[i] != x:
                rotations_bottom += 1
        return min(rotations_top, rotations_bottom)

    # Only values that could be valid candidates are tops[0] and bottoms[0]
    result = check(tops[0])
    if result != -1:
        return result
    elif tops[0] != bottoms[0]:
        return check(bottoms[0])
    return -1

print(minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))  # Output: 2
print(minDominoRotations([1, 2, 1, 2, 1], [2, 1, 2, 1, 2]))  # Output: 2