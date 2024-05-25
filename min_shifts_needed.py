def min_shifts_needed(n, row):
    arts = ['H', 'S', 'P', 'D']
    min_shifts = float('inf')

    for art in arts:
        shifts = 0
        count = row.count(art)
        idx = row.index(art)
        current_shifts = 0

        for i in range(n):
            if row[(idx + i) % n] != art:
                current_shifts += 1

            shifts = min(current_shifts, count - current_shifts)
            if shifts >= min_shifts:
                break

        min_shifts = min(min_shifts, shifts)

    return min_shifts


# Reading input
total_arts = int(input())
row = input().split()

# Calculating and printing the minimum number of shifts needed
result = min_shifts_needed(total_arts, row)
print(result)
