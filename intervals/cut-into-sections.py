def mergeIntervals(intervals):

    if len(intervals) <= 1:
        return intervals

    # Sort intervals based on the start of each interval
    intervals.sort()
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        if merged[-1][1] > intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])

    return merged

def checkValidCuts(n: int, rectangles) :
    vertical = []
    horizontal = []

    # Extract vertical and horizontal intervals
    for rect in rectangles:
        # (StartY, EndY)
        vertical.append([rect[1], rect[3]])  # Vertical view (y-coordinates)
        # (StartX, EndX)
        horizontal.append([rect[0], rect[2]])  # Horizontal view (x-coordinates)

    mergedH = mergeIntervals(horizontal)
    mergedV = mergeIntervals(vertical)

    return len(mergedH) >= 3 or len(mergedV) >= 3


print(checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))  # Output: True
print(checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))  # Output: False
