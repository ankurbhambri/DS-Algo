def letterCombinations(digits):

    res = []

    hm = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def dfs(i, curr):

        if len(curr) == len(digits):
            res.append(curr)
            return

        for c in hm[digits[i]]:
            dfs(i + 1, curr + c)

    if digits:
        dfs(0, "")
    return res


print(letterCombinations("23"))
print(letterCombinations("234"))
print(letterCombinations("2345"))
print(letterCombinations("23456"))
