"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

https://github.com/CodingWithMinmer/CodingWithMinmer/blob/main/1047_remove_all_adjacent_duplicates_in_string/variant_remove_all_1047.hpp

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

"""

class Solution:
    def removeDuplicates(self, s: str) -> str:

        st = []

        for ch in s:

            if st and st[-1] == ch:
                st.pop()

            else:
                st.append(ch)

        return "".join(st)

print(Solution().removeDuplicates("abbaca"))  # Output: "ca"
print(Solution().removeDuplicates("azxxzy"))  # Output: "ay"


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

# Variant: What if we have to remove all adjacent duplicates as we iterate left-to-right?

def remove_all_adjacent_duplicates_variant(s: str) -> str:

    # stack elements: [char, freq]
    stack = []

    for ch in s:

        if not stack:
            stack.append([ch, 1])
            continue

        # same character → increase frequency
        if stack[-1][0] == ch:
            stack[-1][1] += 1
            continue

        # different character → finalize previous run
        if stack[-1][1] > 1:
            stack.pop()

        # now handle current character (possible chain reaction)
        if not stack or stack[-1][0] != ch:
            stack.append([ch, 1])

        else:
            stack[-1][1] += 1

    # final cleanup
    if stack and stack[-1][1] > 1:
        stack.pop()

    # build result
    return "".join(ch for ch, _ in stack)


print(remove_all_adjacent_duplicates_variant("azxxzy")) # Expected output: "ay"
print(remove_all_adjacent_duplicates_variant("abbbacxdd")) # Expected output: "c"