def robotSim(commands, obstacles):

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    obs = set(map(tuple, obstacles))
    x = y = d = 0
    max_dist = 0

    for cmd in commands:
        if cmd == -1:  # Turn right and % 4 is to 
            d = (d + 1) % 4
        elif cmd == -2:  # Turn left
            d = (d - 1) % 4
        else:
            dx, dy = directions[d]  # position
            for _ in range(cmd):
                if (x + dx, y + dy) not in obs:
                    x += dx
                    y += dy
                    max_dist = max(max_dist, x**2 + y**2)

    return max_dist


print(robotSim([4, -1, 3], []))
print(robotSim([4, -1, 4, -2, 4], [[2, 4]]))
print(robotSim([4, -1, 4, -2, 4], [[2, 4], [4, 4]]))

print(
    robotSim(
        [-2, -1, 8, 9, 6],
        [
            [-1, 3],
            [0, 1],
            [-1, 5],
            [-2, -4],
            [5, 4],
            [-2, -3],
            [5, -1],
            [1, -1],
            [5, 5],
            [5, 2],
        ],
    )
)


print(
    robotSim(
        [-2, 8, 3, 7, -1],
        [
            [-4, -1],
            [1, -1],
            [1, 4],
            [5, 0],
            [4, 5],
            [-2, -1],
            [2, -5],
            [5, 1],
            [-3, -1],
            [5, -3],
        ],
    )
)
