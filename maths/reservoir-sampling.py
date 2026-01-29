import random

def reservoir_sampling(stream, k):
    # Pehle k items ko reservoir mein bhar lo
    reservoir = stream[:k]

    # Baaki items ke liye loop chalao
    for i in range(k, len(stream)):
        # i tak koi bhi random index choose karo
        j = random.randint(0, i)
        
        # Agar index k se chhota hai, toh replace kar do
        if j < k:
            reservoir[j] = stream[i]
            
    return reservoir


print(reservoir_sampling([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(reservoir_sampling(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 2))


# Similar problems

# - https://leetcode.com/problems/random-pick-index/

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: 'int') -> 'int':
        count = 0
        result = -1

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # 1/count probability se select karo, if selected, update result
                if random.randint(1, count) == count:
                    result = i

        return result

# - https://leetcode.com/problems/linked-list-random-node/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        i = 1
        res = None
        curr = self.head
        while curr:
            # 1 se i ke beech random number agar 1 aaye
            if random.random() < 1/i:
                res = curr.val
            curr = curr.next
            i += 1
        return res