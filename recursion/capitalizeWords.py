# capitalizeWords Solution


def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])


words = ["i", "am", "learning", "recursion"]
print(capitalizeWords(words))  # ['I', 'AM', 'LEARNING', 'RECURSION']

# similar question


def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


print(capitalizeFirst(["car", "taco", "banana"]))  # ['Car','Taco','Banana']
