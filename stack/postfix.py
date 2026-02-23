"""
= a + b  (infix)

        +
      a   b   

= (a + b) * c 

            *
        +        c
      a    b

= ab+
            +
         a      b

= ab+c* 
            *
        +        c
      a    b

input: ab+
output: binary tree

# + - * /

Precedence = / *

a 
b 

ab+cd-* 

        * 
    +        - 
  a   b     c  d


x+cd* not valid

abc++ ->
        +
    a(8)         +
             b(6)  c(7)

"""

# case 2

# ab+
# expr[i] == +
# Node

# func(Node(expr[i]), expr[i], expr[i + 1])


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(expr):

    st = []  # O(N)

    for i in range(len(expr)):  # O(N)

        if expr[i] not in "/*+-":
            st.append(Node(expr[i]))

        else:
            r = st.pop()
            l = st.pop()
            st.append(Node(expr[i], l, r))

    return st.pop()


# input: binary expression tree
# output: a value of the expression
def eval(root: Node):

    def helper(node: Node):

        if not node.left and not node.right:
            return int(node.val)

        left_val = helper(node.left)
        right_val = helper(node.right)

        if node.val == "+":
            return left_val + right_val

        elif node.val == "-":
            return left_val - right_val

        elif node.val == "*":
            return left_val * right_val

        elif node.val == "/":
            return left_val // right_val

    return helper(root)


expr = "86+97-*"
print(eval(solution(expr)))

expr = "4"
print(eval(solution(expr)))

expr = "86+"
print(eval(solution(expr)))

