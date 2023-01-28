# using iteration
def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False
    return True

print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False

# using recursion
def is_palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
