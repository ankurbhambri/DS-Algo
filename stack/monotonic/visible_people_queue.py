# https://leetcode.com/problems/number-of-visible-people-in-a-queue/


def canSeePersonsCount(heights):

    res = [0] * len(heights)
    st = []

    for i in range(len(heights) - 1, -1, -1):

        while st and st[-1] < heights[i]:
            res[i] += 1
            st.pop()

        if st:
            res[i] += 1

        st.append(heights[i])

    res[-1] = 0

    return res


print(canSeePersonsCount([10, 6, 8, 5, 11, 9]))  # Output: [3,1,2,1,1,0]
print(canSeePersonsCount([5, 1, 2, 3, 10]))  # Output: [4,1,1,1,0]
print(canSeePersonsCount([1, 2, 3, 4, 5]))  # Output: [1,1,1,1,0]
print(canSeePersonsCount([1]))  # Output: [0]
