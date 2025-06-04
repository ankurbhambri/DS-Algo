def run_length_encoding(s: str) -> str:
    n = len(s)
    res = []
    i = 0
    
    while i < n:
        count = 1
        # Count how many times s[i] repeats
        while i + count < n and s[i] == s[i + count]:
            count += 1
        
        # Append count and character
        res.append(str(count))
        res.append(s[i])
        
        # Move i forward by count steps
        i += count
    
    return "".join(res)


print(run_length_encoding("aaaabbcc"))  # Expected: 4a2b2c
print(run_length_encoding("a"))         # Expected: 1a
print(run_length_encoding("abc"))       # Expected: 1a1b1c
print(run_length_encoding(""))          # Expected: ""
print(run_length_encoding("zzzzzzzz"))  # Expected: 8z
