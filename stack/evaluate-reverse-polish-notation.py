def evalRPN(tokens):

    st = []
    for t in tokens:
        if t == "+":
            st.append(st.pop() + st.pop())
        elif t == "-":
            a, b = st.pop(), st.pop()
            st.append(b - a)
        elif t == "*":
            st.append(st.pop() * st.pop())
        elif t == "/":
            a, b = st.pop(), st.pop()
            st.append(int(b / a))
        else:
            st.append(int(t))
    return st[0]


print(evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
print(evalRPN(["4", "3", "-"]))  # Output: 1
print(evalRPN(["10", "6", "9", "3", "/", "-11", "*", "+"]))  # Output: 10
print(evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
