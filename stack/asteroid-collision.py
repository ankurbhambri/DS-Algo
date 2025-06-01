class Solution:
    def asteroidCollision(self, asteroids):
        st = []
        for i in range(len(asteroids)):
            while st and ((asteroids[i] < 0 and asteroids[st[-1]] > 0) or (asteroids[i] > 0 and asteroids[st[-1]] < 0)):

                if abs(asteroids[i]) >= abs(asteroids[st[-1]]):
                    st.pop()
                    st.append(i)
                else:
                    break

            if not st:
                st.append(i)

            if st[-1] != i:
                if st and asteroids[st[-1]] > 0 and asteroids[i] > 0:
                    st.append(i)

                if st and asteroids[st[-1]] < 0 and asteroids[i] < 0:
                    st.append(i)

        return st

print(Solution().asteroidCollision([5, 10, -5]))  # [5, 10]
print(Solution().asteroidCollision([8, -8]))  # []
print(Solution().asteroidCollision([10, 2, -5]))  # [10]
print(Solution().asteroidCollision([-2, -1, 1, 2]))  # [-2, -1, 1, 2]