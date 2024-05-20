# Given two sorted and distinct arrays, find the most common elements.

def solution(arr1, arr2):

  i, j = 0, 0
  res = []

  while i < len(arr1) and j < len(arr2):

      if arr1[i] > arr2[j]:
          j += 1
      elif arr1[i] < arr2[j]:
          i += 1
      else:
          res.append(arr1[i])
          i += 1
          j += 1

  return res

print(solution([1, 2, 4, 5, 6], [2, 4, 6, 8, 10])
