"""
You are playing a video game where you are defending your city from a group of n monsters. 

You are given a O-indexed integer array dist of size n, where dist[i] is the initial distance in meters of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n,
where speed[i] is the speed of the ith monster in meters per minute.

The monsters start moving at minute 0. You have a weapon that you can choose to use at the start of every minute, including minute 0. 
You cannot use the weapon in the middle of a minute. The weapon can eliminate any monster that is still alive. You lose when any monster reaches your city. 

If a monster reaches the city exactly at the start of a minute, it counts as a loss, and the game ends before you can use your weapon in that minute.
Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters before they reach the city.

Example 1:
Input: dist = [1,3,4], speed = [1,1,1]
Output: 3
Explanation:
At the start of minute 0, the distances of the monsters are [1,3,4], you eliminate the first monster.
At the start of minute 1, the distances of the monsters are [X,2,3], you don't do anything.
At the start of minute 2, the distances of the monsters are [X,1,2], you eliminate the second monster.
At the start of minute 3, the distances of the monsters are [X,X,1], you eliminate the third monster.
All 3 monsters can be eliminated.

"""


def eliminateMaximum(dist, speed):

    times = [dist[i] // speed[i] for i in range(len(dist))]

    times.sort()

    eliminated = 0
    for minute, time in enumerate(times):
        if minute < time:
            eliminated += 1
        else:
            break  # A monster reaches the city, stop

    return eliminated


# Example Usage:
# dist = [1, 3, 4]
# speed = [1, 1, 1]
# print(eliminateMaximum(dist, speed))  # Output: 3

# dist = [1, 1, 2, 3]
# speed = [1, 1, 1, 1]
# print(eliminateMaximum(dist, speed))  # Output: 1

# dist = [3, 2, 4]
# speed = [5, 3, 2]
# print(eliminateMaximum(dist, speed))  # Output: 0


# similar question

# https://codeforces.com/problemset/problem/1923/B

# B. Monsters Attack!


def can_kill_all_monsters(test_cases):

    n, k = test_cases["n"], test_cases["k"]
    health = test_cases["health"]
    positions = test_cases["positions"]

    move_right = [0] * (n + 1)

    for i in range(n):
        move_right[abs(positions[i])] += health[i]

    power = k
    for i in range(1, n + 1):
        if power < move_right[i]:
            return "NO"

        power -= move_right[i]
        power += k

    return "YES"


# Example Input
t = 5
test_cases = [
    {"n": 3, "k": 2, "health": [1, 2, 3], "positions": [-1, 2, 3]},
    {"n": 2, "k": 1, "health": [1, 1], "positions": [-1, 1]},
    {"n": 4, "k": 10, "health": [3, 4, 2, 5], "positions": [-3, -2, 1, 3]},
    {"n": 5, "k": 3, "health": [2, 1, 3, 2, 5], "positions": [-3, -2, 3, 4, 5]},
    {"n": 2, "k": 1, "health": [1, 2], "positions": [1, 2]},
]


for t in test_cases:
    print(can_kill_all_monsters(t))


# https://codeforces.com/problemset/problem/1922/D
# D. Berserk Monsters

