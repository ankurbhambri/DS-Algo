import time

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])

    result.extend(right[j:])
    
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

arr = [38, 27, 43, 3, 9, 82, 10]

start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

print("Original array:", arr)
print("Sorted array:", sorted_arr)
print("Time taken to sort:", end_time - start_time, "seconds")


# Another way

def sortArray(nums):

        if len(nums) > 1:

            m = len(nums) // 2

            l = nums[:m]
            r = nums[m:]
            
            sortArray(l)
            sortArray(r)
            
            i = j = k = 0
            
            while i < len(l) and j < len(r):

                if l[i] > r[j]:    
                    nums[k] = r[j]
                    j += 1
                    
                else:
                    nums[k] = l[i]
                    i += 1

                k += 1
                
            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1

        return nums

start_time = time.time()

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
print("Sorted array:", sortArray(arr))
end_time = time.time()
print("Time taken to sort:", end_time - start_time, "seconds")
