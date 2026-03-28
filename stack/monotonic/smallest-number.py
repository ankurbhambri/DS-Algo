# https://leetcode.com/problems/construct-smallest-number-from-di-string/description


def smallestNumber(pattern):

    stack = []
    result = []
    num = 1  # Start numbering from 1

    for i in range(len(pattern) + 1):
        stack.append(str(num))  # Push the next available number
        num += 1

        if i == len(pattern) or pattern[i] == "I":  # Process decreasing segment
            while stack:
                result.append(stack.pop())

    return "".join(result)


print(smallestNumber("IIIDIDDD"))  # 123549876
print(smallestNumber("DDD"))  # 4321
print(smallestNumber("III"))  # 123
print(smallestNumber("DDI"))  # 3210
print(smallestNumber("D"))  # 21
print(smallestNumber("I"))  # 12
print(smallestNumber("ID"))  # 132
print(smallestNumber("DI"))  # 213
