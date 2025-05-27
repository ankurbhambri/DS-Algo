"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

https://github.com/CodingWithMinmer/CodingWithMinmer/blob/main/1047_remove_all_adjacent_duplicates_in_string/variant_remove_all_1047.hpp

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

"""


def removeDuplicates(s):
    st = []

    for c in s:
        if st and st[-1] == c:
            st.pop()
        else:
            st.append(c)

    return "".join(st)


# print(removeDuplicates("abbaca"))  # Output: "ca"
# print(removeDuplicates("azxxzy"))  # Output: "ay"


# Variant - What if we had to remove all adjacent duplicates as you iterate.

def func(s):

    frq_list = [] # ch, freq

    for i in range(len(s)):

        if frq_list and frq_list[-1][0] != s[i]:

            if frq_list[-1][1] > 1:
                frq_list.pop()
            
        if frq_list and frq_list[-1][0] == s[i]:
            frq_list[-1][1] += 1
    
        else:
            frq_list.append([s[i], 1])

    if frq_list and frq_list[-1][1] > 1:
        frq_list.pop()
    
    return "".join([a for a, b in frq_list]) if frq_list else "None"

print(func("azxxzy"))  # Output: "ay"
print(func("abbaxx"))  # Output: ""
print(func("aabbccdd"))  # Output: ""
print(func("aaabbaad"))  # Output: "d"
print(func("abcdefg"))  # Output: "abcdefg"
print(func("abbcddeff"))  # Output: "ace"
print(func("abcdeffedcba"))  # Output: ""
print(func("aabccddeeffbbbbbbbbbf"))  # Output: "f"
print(func("abbbacca"))  # Output: "ac"
print(func("abccba"))  # Output: ""
print(func("abbbacxdd")) # "cx"

'''
std::string s = "azxxxzy";
assert("ay" == remove_all_adjacent_duplicates_variant_1047(s));

s = "abbaxx";
assert(remove_all_adjacent_duplicates_variant_1047(s).empty());

s = "aabbccdd";
assert(remove_all_adjacent_duplicates_variant_1047(s).empty());

s = "aaabbaad";
assert("d" == remove_all_adjacent_duplicates_variant_1047(s));

s = "abcdefg";
assert("abcdefg" == remove_all_adjacent_duplicates_variant_1047(s));

s = "abbcddeff";
assert("ace" == remove_all_adjacent_duplicates_variant_1047(s));

s = "abcdeffedcba";
assert(remove_all_adjacent_duplicates_variant_1047(s).empty());

s = "aabccddeeffbbbbbbbbbf";
assert("f" == remove_all_adjacent_duplicates_variant_1047(s));

s = "abbbacca"; // Cannot pick and choose duplicates in the middle to delete first
assert("a" == remove_all_adjacent_duplicates_variant_1047(s));

s = "abccba";
assert("" == remove_all_adjacent_duplicates_variant_1047(s));

s = "abbbacxdd";
assert("cx" == remove_all_adjacent_duplicates_variant_1047(s));
'''