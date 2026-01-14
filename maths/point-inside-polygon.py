# https://www.youtube.com/watch?v=RSXM9bgqxJM

# Ray casting algorithm

def point_in_polygon(point, edges):
    x, y = point
    cnt = 0

    n = len(edges)
    px1, py1 = edges[0]

    for i in range(n + 1):

        px2, py2 = edges[i % n]

        if min(py1, py2) < y <= max(py1, py2):
            if x <= max(px1, px2):
                if py1 != py2:
                    xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                if px1 == px2 or x <= xinters:
                    cnt += 1

        px1, py1 = px2, py2

    # if count is even, point is outside, else inside
    return "Outside" if cnt % 2 == 0 else "Inside"


print(point_in_polygon((10, 15), [(0, 0), (20, 0), (10, 30)]))  # Inside
print(point_in_polygon((30, 15), [(0, 0), (20, 0), (10, 30)]))  # Outside