# https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/


def findTriplets(arr):
    arr.sort()
    n = len(arr)
    triplets = []

    for i in range(n - 2):
        # To avoid duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])

                # Move the left and right pointers to the next different numbers
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets


# Test cases
print(findTriplets([0, -1, 2, -3, 1]))  # Output: [[-3, 1, 2], [-1, 0, 1]]
print(findTriplets([1, -2, 1, 0, 5]))  # Output: [[-2, 1, 1]]
print(findTriplets([2, 3, 1, 0, 5]))  # Output: []
