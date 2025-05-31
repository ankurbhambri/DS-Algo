# https://leetcode.ca/all/370.html


def getModifiedArray(length, updates):

    result = [0] * length
    
    for start, end, inc in updates:
        result[start] += inc
        if end + 1 < length:
            result[end + 1] -= inc
    
    # Apply prefix sum
    for i in range(1, length):
        result[i] += result[i - 1]
    
    return result


print(getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])) # Output: [-2, 0, 3, 5, 3]
print(getModifiedArray(3, [[0, 1, 100], [1, 2, 100]])) # Output: [100, 200, 100]