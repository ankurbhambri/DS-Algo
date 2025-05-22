# https://leetcode.com/problems/permutation-sequence/description/

def getPermutation(n, k):
    # Create list of numbers 1 to n
    numbers = list(range(1, n + 1))
    k = k - 1  # Convert to 0-based index
    factorial = 1
    # Calculate (n-1)! for the first step
    for i in range(1, n):
        factorial *= i
    
    result = []
    # Build permutation
    for i in range(n-1, -1, -1):  # From n-1 down to 0
        if i == 0:  # Last number
            result.append(str(numbers[0]))
            break
        # Get index of current digit
        index = k // factorial
        k = k % factorial
        factorial = factorial // i
        # Append the digit and remove it from numbers
        result.append(str(numbers[index]))
        numbers.pop(index)
    
    return ''.join(result)

print(getPermutation(3, 3))  # Output: "213"