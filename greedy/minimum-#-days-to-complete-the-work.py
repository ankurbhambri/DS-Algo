# https://www.geeksforgeeks.org/minimum-number-of-days-required-to-complete-the-work/

def min_days_to_complete(N, D1, D2):
    # Combine tasks and sort by D1 (non-decreasing required)
    tasks = sorted(zip(D1, D2))

    current_day = 0

    for d1, d2 in tasks:
        # Choose the earliest valid day >= current_day
        if d2 >= current_day:
            current_day = d2
        else:
            current_day = d1

    return current_day


N = 3
D1 = [5, 3, 4]
D2 = [2, 1, 2]

print(min_days_to_complete(N, D1, D2))  # Output: 2

N = 6
D1 = [3, 3, 4, 4, 5, 5]
D2 = [1, 2, 1, 2, 4, 4]

print(min_days_to_complete(N, D1, D2))  # Output: 4
