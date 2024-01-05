arr = [1, 2, 3, 0, 3]
arr1 = [1, 2, 3, 0, 3]

# prefix
for i in range(1, len(arr1)):
    arr1[i] += arr1[i - 1]

# suffix
for i in range(len(arr) - 2, -1, -1):
    arr[i] += arr[i + 1]

print(arr1, arr)
