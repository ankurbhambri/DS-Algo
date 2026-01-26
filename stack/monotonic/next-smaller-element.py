# Nearest Smaller to Left (NSL)

'''
Forward Loop: 0 se n-1 tak chalo.
Pop Condition: Jab tak stack ka top element current number se bada ya barabar (stack[-1] >= nums[i]) hai, use nikal do. Kyunki humein "chota" chahiye.
Answer: Stack ka top hi aapka NSL hai.
'''

def get_left_smaller(nums):

    stack = []
    n = len(nums)
    nsl = [-1] * n

    for i in range(n):

        while stack and stack[-1] >= nums[i]:
            stack.pop()

        if stack:
            nsl[i] = stack[-1]

        stack.append(nums[i])

    return nsl

print(get_left_smaller([4, 5, 2, 10, 8]))  # Output: [-1,4,-1,2,2]
print(get_left_smaller([2, 7, 3, 5, 4, 6, 8]))  # Output: [-1,2,2,3,3,4,6]


# Nearest Smaller to Right (NSR)

'''
Backward Loop: n-1 se 0 tak chalo.
Pop Condition: Jab tak stack ka top element current number se bada ya barabar (stack[-1] >= nums[i]) hai, use nikal do.
Answer: Stack ka top hi aapka NSR hai.
'''

def get_right_smaller(nums):

    stack = []
    n = len(nums)
    nsr = [-1] * n

    for i in range(n - 1, -1, -1):

        while stack and stack[-1] >= nums[i]:
            stack.pop()

        if stack:
            nsr[i] = stack[-1]

        stack.append(nums[i])

    return nsr

print(get_right_smaller([4, 5, 2, 10, 8]))  # Output: [2,2,-1,8,-1]
print(get_right_smaller([2, 7, 3, 5, 4, 6, 8]))  # Output: [-1,3,-1,4,-1,-1,-1]