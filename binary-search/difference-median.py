# https://www.geeksforgeeks.org/median-of-difference-of-all-pairs-from-an-arr/
# https://discuss.codechef.com/t/formula-n-n-1-2/9774/2


def count_pairs_with_diff_leq(arr, value):
    count = 0
    n = len(arr)
    j = 0
    for i in range(n):
        while j < n and arr[j] - arr[i] <= value:
            j += 1
        count += j - i - 1
    return count


def find_median_difference(arr):
    
    n = len(arr)
    arr.sort()

    low = 0
    high = arr[-1] - arr[0]

    while low <= high:
        mid = (low + high) // 2
        c = count_pairs_with_diff_leq(arr, mid)
        if c < n * (n - 1) // 2 // 2:
            low = mid + 1
        else:
            high = mid - 1

    return low


arr = [1, 2, 3, 4, 5, 6, 7]
median_difference = find_median_difference(arr)
print(f"Median of differences: {median_difference}")
