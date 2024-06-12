# https://leetcode.com/problems/remove-k-digits/


def removeKdigits(num, k):

    st = list()
    for n in num:
        while st and k and st[-1] > n:
            st.pop()
            k -= 1

        if st or n is not "0":  # prevent leading zeros
            st.append(n)

    if k:
        st = st[0:-k]

    return "".join(st) or "0"


print(removeKdigits("1432219", 3))  # "1219"
print(removeKdigits("10200", 1))  # "200"
