def matching_pairs(s, t):

    s = [i for i in s]

    a, b = 0, 0
    res = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            j = i
            while j < len(s):
                if s[j] == t[i]:
                    s[i], s[j] = s[j], s[i]
                    res += 1
                    break
                else:
                    j += 1

    s = "".join(s)
    print(s)
    return res


s_1, t_1 = "abcde", "adcbe"
# expected_1 = 5
print(matching_pairs(s_1, t_1))


s_2, t_2 = "abcd", "abcd"
# expected_2 = 2
print(matching_pairs(s_2, t_2))
