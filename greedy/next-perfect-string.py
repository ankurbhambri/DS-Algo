"""
A company is developing a system that generates "perfect strings." A perfect string is defined as a string where no two adjacent characters are the same. 

Given an input string, which may or may not already be perfect, your task is to return the lexicographically smallest perfect string that is greater than the given string. 

If no such string exists, return "-1".

Examples:
1. Input: "abzzzcd" -> Output: "acababa"
2. Input: "zzab" -> Output: "-1" (No valid perfect string exists)

"""

def next_perfect_string(s):
    s = list(s)
    n = len(s)

    # Try to modify the string from right to left
    for i in range(n - 1, -1, -1):
        original_char = s[i]
        
        # Try each possible larger character
        for next_char_ord in range(ord(original_char) + 1, ord('z') + 1):
            next_char = chr(next_char_ord)
            
            # Check if replacing with this character would be valid
            if i == 0 or s[i - 1] != next_char:
                # Make the change
                s[i] = next_char
                
                # Reset all characters to the right
                for j in range(i + 1, n):
                    s[j] = 'a'
                
                # Fix adjacent duplicates to make string perfect
                for j in range(1, n):
                    if s[j] == s[j - 1]:
                        if s[j] == 'z':  # Cannot increment further
                            break
                        s[j] = chr(ord(s[j]) + 1)
                
                # Check if string is perfect now
                perfect = True
                for j in range(1, n):
                    if s[j] == s[j - 1]:
                        perfect = False
                        break
                
                if perfect:
                    return ''.join(s)
                
                # Reset for next iteration
                s[i] = original_char
    
    return "-1"  # No valid perfect string found
    
    
print(next_perfect_string("abzzzcd"))  # Output: acababa
print(next_perfect_string("zzab")) # Output: -1
print(f"Input: abzzzcd, Output: {next_perfect_string('abzzzcd')}")
print(f"Input: zzab, Output: {next_perfect_string('zzab')}")
print(f"Input: fedcba, Output: {next_perfect_string('fedcba')}")
print(f"Input: abc, Output: {next_perfect_string('abc')}")
print(f"Input: az, Output: {next_perfect_string('az')}")
print(f"Input: z, Output: {next_perfect_string('z')}")