# https://leetcode.com/problems/count-number-of-teams/


# Brute force - TL error
# idea three loops and checking increasing or decreasing order of elements.

def numTeams(self, rating: List[int]) -> int:
    n = len(rating)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                    count += 1

    return count


# O(N^2) approach
def numTeams(self, rating: List[int]) -> int:
    n = len(rating)
    count = 0

    for j in range(n):
        left_less = left_greater = 0
        right_less = right_greater = 0

        # Count soldiers to the left of j
        for i in range(j):
            if rating[i] < rating[j]:
                left_less += 1
            elif rating[i] > rating[j]:
                left_greater += 1

        # Count soldiers to the right of j
        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                right_less += 1
            elif rating[k] > rating[j]:
                right_greater += 1

        # Calculate the number of valid teams
        count += left_less * right_greater + left_greater * right_less

    return count
