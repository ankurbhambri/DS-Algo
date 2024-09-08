# https://leetcode.com/problems/minimum-window-substring/


def min_length_substring(s, t):
    if not s or not t:
        return ""

    dict_t = {}
    for i in t:
        dict_t[i] = dict_t.get(i, 0) + 1

    window_counts = {}

    required = len(dict_t)

    formed = 0

    ans = [float("inf"), None, None]

    l = 0

    for r in range(len(s)):
        # Add one character from the right to the window
        window_counts[s[r]] = 1 + window_counts.get(s[r], 0)

        # If the frequency of the current s[r] added equals to the desired count in t then increment the formed count by 1
        if s[r] in dict_t and window_counts[s[r]] == dict_t[s[r]]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while formed == required:

            # Save the smallest window until now
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[s[l]] -= 1
            if s[l] in dict_t and window_counts[s[l]] < dict_t[s[l]]:
                formed -= 1

            l += 1

    return -1 if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


s = "dcbefebce"
t = "fd"
print(min_length_substring(s, t))
# output = 5


s = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
t = "cbccfafebccdccebdd"
print(min_length_substring(s, t))
