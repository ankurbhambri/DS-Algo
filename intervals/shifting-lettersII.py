# https://leetcode.com/problems/shifting-letters-ii/description


def shiftingLetters(s, shifts):

    arr = [0] * len(s)

    for i, j, d in shifts:
        if d == 0:
            arr[i] -= 1
            if j + 1 <= len(s) - 1:
                arr[j + 1] += 1
        else:
            arr[i] += 1
            if j + 1 <= len(s) - 1:
                arr[j + 1] -= 1

    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    # just changing the value after shifting
    for i, op in enumerate(arr):
        s = s[:i] + chr((ord(s[i]) - ord("a") + op) % 26 + ord("a")) + s[i + 1 :]

    return s


print(shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]))  # Output: "ace"
print(shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]))  # Output: "catz"
