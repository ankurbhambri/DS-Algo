# Python Program to Flatten a Nested List using Recursion

def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))  # Recursively flatten nested list
        else:
            flattened.append(item)
    return flattened

# Example usage:
nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
flattened_list = flatten_list(nested_list)
print("Original nested list:", nested_list)
print("Flattened list:", flattened_list)
