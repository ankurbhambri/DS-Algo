# Time: O(n)
# Space: O(n)


def countPalindromicSubsequence(s):

    first = [float("inf")] * 26
    last = [float("-inf")] * 26

    for i in range(len(s)):
        curr = ord(s[i]) - ord("a")
        first[curr] = min(first[curr], i)
        last[curr] = max(last[curr], i)

    ans = 0
    for i in range(26):

        if first[i] == float("inf") or last[i] == float("-inf"):
            continue

        between = set()
        for j in range(first[i] + 1, last[i]):
            between.add(s[j])

        ans += len(between)

    return ans
