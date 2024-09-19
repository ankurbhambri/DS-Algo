def diffWaysToCompute(expression):
    res = []
    for i in range(len(expression)):
        if expression[i] in "*+-":
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i + 1 :])
            for a in left:
                for b in right:
                    if expression[i] == "+":
                        res.append(a + b)
                    elif expression[i] == "-":
                        res.append(a - b)
                    elif expression[i] == "*":
                        res.append(a * b)
    if not res:
        res.append(int(expression))

    return res


# TC - O(2^N)
# SC - O(2^N)
print(diffWaysToCompute("2-1-1"))
print(diffWaysToCompute("2*3-4*5"))
