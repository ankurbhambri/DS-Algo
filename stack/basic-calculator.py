# https://leetcode.com/problems/basic-calculator-ii/


def solution(s):

    curr = 0
    ope = "+"
    st = []

    for i in range(len(s)):

        if s[i].isdigit():
            curr = curr * 10 + int(s[i])

        if s[i] in "+-*/" or i == len(s) - 1:

            if ope == "-":
                st.append(-curr)
            elif ope == "*":
                st.append(st.pop() * curr)
            elif ope == "/":
                st.append(int(st.pop() / curr))
            else:
                st.append(curr)

            curr = 0
            ope = s[i]

    return sum(st)


print(solution("3+2*2"))  # 7
print(solution("0-213456789"))  # -213456789
print(solution("3/2"))  # 1
print(solution("3+5/2"))  # 5
print(solution("3+5/2*2"))  # 8
print(solution("3+5/2*2-1"))  # 7
