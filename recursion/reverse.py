def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]


def reverse_stack(st):
    if len(st) == 0:
        return st
    return reverse_stack(st[1:]) + [st[0]]

print(reverse_string("hello"))  # Output: "olleh"
print(reverse_stack([1,2,3,4])) # Output: [4, 3, 2, 1]
