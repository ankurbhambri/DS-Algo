# https://leetcode.com/discuss/interview-question/1364630/oa-max-number-of-non-intersecting-elements-of-len-2-having-same-sum


def solution(A):
    count = 0
    sums = {}
    prev_sum = -1
    for i in range(len(A) - 1):
        current_sum = A[i] + A[i + 1]

        # Check if current_sum is already in sums dictionary
        if current_sum not in sums:
            sums[current_sum] = 1
            prev_sum = current_sum
        elif current_sum != prev_sum:
            sums[current_sum] += 1
            prev_sum = current_sum
        else:
            prev_sum = -1

        # Update count with the maximum value found in sums dictionary
        count = max(count, sums[current_sum])

    return count


print(solution([9, 9, 9, 9]))
print(solution([5, 3, 1, 3, 2, 3]))
print(solution([10, 1, 3, 1, 2, 2, 1, 0, 4]))
