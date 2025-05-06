# https://leetcode.com/problems/decode-string/

def decode_string(s):

    stack = []
    curr_num = 0
    curr_str = ''
    
    for char in s:

        if char.isdigit():
            curr_num = curr_num * 10 + int(char)

        elif char == '[':
            # Push the current string and number onto the stack
            stack.append((curr_str, curr_num))
            # Reset for the new bracketed part
            curr_str = ''
            curr_num = 0

        elif char == ']':
            # Pop from stack and build new string
            last_str, num = stack.pop()
            curr_str = last_str + curr_str * num
        else:
            curr_str += char
    
    return curr_str


print(decode_string("3[a2[c]]"))  # Output: "accaccacc"
print(decode_string("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
print(decode_string("abc3[cd]xyz"))  # Output: "abccdcdcdxyz"
print(decode_string("3[a]2[bc]"))  # Output: "aaabcbc"
