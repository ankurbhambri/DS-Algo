# https://leetcode.com/problems/minimum-window-substring/


from collections import Counter


def minWindow(s, t):

    if not s or not t:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    formed = 0
    window_counts = {}

    ans = [float("inf"), None, None]

    l, r = 0, 0

    while r < len(s):
        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = 1 + window_counts.get(character, 0)

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till then our condition is true for need == required.
        while formed == required:

            character = s[l]

            # Save the smallest window until now comparing with curr window size and previous window size.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                # Here condition will break because we removed a character from the window which is needed to be in the window.
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1

        # Keep expanding the window once we are done contracting.
        r += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
