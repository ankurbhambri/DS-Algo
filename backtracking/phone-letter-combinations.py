# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits):

        # If input is empty, return empty list
        if not digits:
            return []

        # Phone map
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = []

        # Backtracking function
        def backtrack(index, path):

            # If current combination length equals digits length
            if index == len(digits):
                res.append("".join(path))
                return

            # Get letters for current digit
            letters = phone_map[digits[index]]
            for ch in letters:
                path.append(ch)           # choose the letter
                backtrack(index + 1, path)  # go to next digit
                path.pop()                # backtrack

        backtrack(0, [])
        return res


print(Solution().letterCombinations("23")) # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(Solution().letterCombinations("234")) # ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
print(Solution().letterCombinations("2345")) # ['adgj', 'adgk', 'adgl', 'adhj', 'adhk', 'adhl', 'adij', 'adik', 'adil', 'aegj', 'aegk', 'aegl', 'aehj', 'aehk', 'aehl', 'aeij', 'aeik', 'aeil', 'afgj', 'afgk', 'afgl', 'afhj', 'afhk', 'afhl', 'afij', 'afik', 'afil', 'bdgj', 'bdgk', 'bdgl', 'bdhj', 'bdhk', 'bdhl', 'bdij', 'bdik', 'bdil', 'begj', 'begk', 'begl', 'behj', 'behk', 'behl', 'beij', 'beik', 'beil', 'bfgj', 'bfgk', 'bfgl', 'bfhj', 'bfhk', 'bfhl', 'bfij', 'bfik', 'bfil']
print(Solution().letterCombinations("23456")) # ['adgjm', 'adgjn', 'adgjo', 'adgkm', 'adgkn', 'adgko', 'adglm', 'adgln', 'adglo', 'adhjm', 'adhjn', 'adhjo', 'adhkm', 'adhkn', 'adhko', 'adhlm', 'adhln', 'adhlo', 'adijm', 'adijn', 'adijo', 'adikm', 'adikn', 'adiko', 'adil...