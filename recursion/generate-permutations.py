def generate_permutations(arr, path=[]):
    if not arr:
        print(path)
        return

    for i in range(len(arr)):
        # Choose arr[i] and recurse with the rest of the elements
        mid = arr[i]
        generate_permutations(arr[:i] + arr[i+1:], path + [mid])

# Example usage
data = [1, 2, 3, 4]
generate_permutations(data)

data = ["1", "2", "3"]
generate_permutations(data)
