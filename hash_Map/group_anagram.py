# https://leetcode.com/problems/group-anagrams/


def groupAnagrams(words):
    res = {}
    for i in words:
        temp = [0] * 26
        for c in i:
            temp[ord("a") - ord(c)] += 1
        temp = tuple(temp)
        if temp in res:
            res[temp].append(i)
        else:
            res[temp] = [i]
    return list(res.values())


# [["eat","tea","ate"],["tan","nat"],["bat"]]
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [[""]]
print(groupAnagrams([""]))
# [["a"]]
print(groupAnagrams(["a"]))
