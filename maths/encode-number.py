# https://leetcode.com/problems/build-array-from-permutation/

def buildArray(nums):

    for i in range(len(nums)):

        nums[i] += (1024 * (nums[nums[i]] % 1024))

    for i in range(len(nums)):
        nums[i] //= 1024

    return nums

print(buildArray([0,2,1,5,3,4]))
print(buildArray([5,0,1,2,3,4]))
