"""
You are given a number line represented by indices from 0 to length - 1. Initially, all positions are uncoloured. 
You are also given a list of queries. Each query is in the form [coord, color], which means: 
Paint the position coord on the number line with the specified color. If that position already had a color, overwrite it. 

After processing each query, you must: 
• Count how many consecutive pairs of coordinates have the same color (i.e., for any i, if both position i and i+1 have the same color, count it as one pair). 
• Return the number of such same-color consecutive coordinates pairs after each query. 

Input 
• length: an integer (1 ≤ length ≤ 10⁹) 
• queries: a list of queries where each query is [coord, color] 
• 1 ≤ queries.length ≤ 10⁵ • 0 ≤ coord < length 
• 1 ≤ color ≤ 10⁹

Input: length = 4, queries = [[0, 2], [1, 2], [3, 1], [1, 1]]

Query           Action                  Neighbors               Total Pairs

[0, 2]      Index 0 becomes color 2     None                        0
[1, 2]      Index 1 becomes color 2     Matches index 0             1
[3, 1]      Index 3 becomes color 1     None                        1
[1, 1]      Index 1 changes 2 -> 1      Loses match with 0;         0
                                        No match with 2 or 0

Result: [0, 1, 1, 0]

Output:
    Return an array of integers of the same length as queries, where each element is the count of same-color adjacent pairs after processing that query.

"""


def colorTheArray(length, queries):

    count = 0
    colors = {}  # coord -> color
    result = []

    for pos, color in queries:

        old_color = colors.get(pos, 0)

        # Remove old contributions from neighbors
        if old_color:

            if colors.get(pos - 1) == old_color:
                count -= 1

            if colors.get(pos + 1) == old_color:
                count -= 1

        # Paint with new color
        colors[pos] = color

        # Add new contributions from neighbors
        if colors.get(pos - 1) == color:
            count += 1

        if colors.get(pos + 1) == color:
            count += 1

        result.append(count)

    return result


print(colorTheArray(1, [[0, 100000]])) # [0]
print(colorTheArray(4, [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]])) # [0, 1, 1, 0, 2]