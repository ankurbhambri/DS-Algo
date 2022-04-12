'''
S1 and S2 given strings we have to convert S2 to S1 using delete, insert, replace operations and find the min count of operations.
'''
# To Down approach
def findMinOperations_DP(s1, s2, i1, i2, dp):
    if i1 == len(s1):
        return len(s2) - i2
    if i2 == len(s2):
        return len(s1) - i1
    if s1[i1] == s2[i2]:
        return findMinOperations_DP(s1, s2, i1 + 1, i2 + 1, dp)
    else:
        key = str(i1) + str(i2)
        if key not in dp:
            deleteOp = 1 + findMinOperations_DP(s1, s2, i1, i2 + 1, dp)
            insertOp = 1 + findMinOperations_DP(s1, s2, i1 + 1, i2, dp)
            replaceOp = 1 + findMinOperations_DP(s1, s2, i1 + 1, i2 + 1, dp)
            dp[key] = min(deleteOp, insertOp, replaceOp)
        return dp[key]


print(findMinOperations_DP('catch', 'catrh', 0, 0, {}))
print(findMinOperations_DP('table', 'tbres', 0, 0, {}))


# Botoom Up approach
def findMinOperation_TB(s1, s2, tb):
    for i1 in range(len(s1) + 1):
        key = str(i1) + '0'
        tb[key] = i1
    for i2 in range(len(s2) + 1):
        key = '0' + str(i2)
        tb[key] = i2

    for i1 in range(1, len(s1) + 1):
        for i2 in range(1, len(s2) + 1):
            if s1[i1 - 1] == s2[i2 - 1]:
                key = str(i1) + str(i2)
                key1 = str(i1 - 1) + str(i2 - 1)
                tb[key] = tb[key1]
            else:
                key = str(i1) + str(i2)
                keyD = str(i1 - 1) + str(i2)
                keyI = str(i1) + str(i2 - 1)
                keyR = str(i1 - 1) + str(i2 - 1)
                tb[key] = 1 + min(
                    tb[keyD],
                    min(tb[keyI], tb[keyR]),
                )
    key = str(len(s1)) + str(len(s2))
    return tb[key]


print(findMinOperation_TB('catch', 'catrh', {}))
print(findMinOperation_TB('table', 'tbres', {}))

# Another Botoom Up approach
# Time Complexity: O(m x n)
# Auxiliary Space: O(m x n)
def editDistDP(str1, str2):
    # Create a table to store results of subproblems
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],  # Insert
                    dp[i - 1][j],  # Remove
                    dp[i - 1][j - 1],
                )  # Replace)

    return dp[m][n]


print(editDistDP('catch', 'catrh'))
print(editDistDP('table', 'tbres'))
print(editDistDP('sunday', 'saturday'))
print(editDistDP('food', 'money'))
