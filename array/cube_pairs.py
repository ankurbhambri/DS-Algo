# Print all possible integer solutions for a^3 + b^3 = c^3 + d^3 where a,b,c,d can be integers 1 - 1000


def find_solutions():

    cube_sums = {}

    # Iterate over all possible pairs (a, b)
    for a in range(1, 1001):
        for b in range(1, 1001):
            sum_cubes = a**3 + b**3

            if sum_cubes not in cube_sums:
                cube_sums[sum_cubes] = [(a, b)]
            else:
                cube_sums[sum_cubes].append((a, b))

    # Iterate through the dictionary and print all matching pairs
    for sum_cubes, pairs in cube_sums.items():
        if len(pairs) > 1:
            for i in range(1, len(pairs)):
                (a, b) = pairs[i - 1]
                (c, d) = pairs[i]
                print(f"a = {a}, b = {b}, c = {c}, d = {d}")


find_solutions()
