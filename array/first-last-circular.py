"""
Given an array of strings → create a new array where each element = first char of current + last char of next. Circular wrap at the end.

Example: ["cat", "dog", "ferret", "scorpion"] → ["cg", "dt", "fn", "st"]
"""


def first_last_circular(words):
    n = len(words)
    res = []
    for i in range(n):
        res.append(words[i][0] + words[(i + 1) % n][-1]) # circular wrap using modulo
    return res


print(first_last_circular(["cat", "dog", "ferret", "scorpion"]))  # ['cg', 'dt', 'fn', 'st']