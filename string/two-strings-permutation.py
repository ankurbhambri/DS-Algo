from collections import Counter


def are_permutations_counting(str1, str2):
    # If lengths are different, they cannot be permutations
    if len(str1) != len(str2):
        return False

    # Create a frequency dictionary for each string
    char_count1 = Counter(str1)
    char_count2 = Counter(str2)

    # Count characters in the first string
    # for char in str1:
    #     char_count1[char] = char_count1.get(char, 0) + 1

    # # Count characters in the second string
    # for char in str2:
    #     char_count2[char] = char_count2.get(char, 0) + 1

    # Compare the two frequency dictionaries
    return char_count1 == char_count2


# Example usage
str1 = "listen"
str2 = "silent"
print(are_permutations_counting(str1, str2))  # Output: True
