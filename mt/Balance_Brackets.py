def isBalanced(s):

    c = {"]": "[", "}": "{", ")": "("}
    st = []

    for w in s:
        if w in c:
            if st and st[-1] == c[w]:
                st.pop()
            else:
                return False
        else:
            st.append(w)

    return len(st) == 0


print(isBalanced("{[(])}"))  # False
print(isBalanced("{{[[(())]]}}"))  # True
