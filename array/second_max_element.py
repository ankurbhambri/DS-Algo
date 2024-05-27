# Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array. 

def solution(arr):
  l, s = 0, 0
  for i in arr:
      if i > l:
          s = l
          l = i
      elif i > s and i != l:
          s = i
  return s

print(solution([12, 35, 1, 10, 34, 1]))
