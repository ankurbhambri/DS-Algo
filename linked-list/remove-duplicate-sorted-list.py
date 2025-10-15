# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

def deleteDuplicates(head):
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        cur = cur.next
    return head


# Similar with array

# https://www.geeksforgeeks.org/dsa/remove-duplicates-sorted-array/

def removeDuplicates(nums):
    if not nums:
        return 0

    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j

print(removeDuplicates([1, 1, 2]))  # 2
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # 5
