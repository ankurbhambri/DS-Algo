# Find the maximum number that can be constructed from a string of digits.


def solution(w):
    freq = {}
    for c in w:  # on
        freq[c] = 1 + freq.get(c, 0)

    res = ""
    for i in range(9, -1, -1):
        i = str(i)
        if i in freq:
            res += freq[i] * i

    return int(res)


print(solution("9234767890"))
