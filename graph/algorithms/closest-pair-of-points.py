import math


# O(n^2) complexity kinda brute force method
def dist(p1, p2):
    return math.sqrt(((p2[1] - p1[1]) ** 2) + ((p2[0] - p1[0]) ** 2))


def closest_brute_force(points):

    min_dist = float("inf")
    p1 = None
    p2 = None

    for i in range(len(points)):

        for j in range(i + 1, len(points)):

            d = dist(points[i], points[j])

            if d < min_dist:
                min_dist = d
                p1 = points[i]
                p2 = points[j]

    return p1, p2, min_dist
