
'''
Given an array with N integers, starting index S and a value X. You are playing game in which you start from S and first move is always odd. 

If the move is odd you can jump to first index on the left which has value A[idx]+1. If the move is even you the same on right side. 

Whenever we make a jump update the previous position by X. Output the end position when you can not make any jump. 

If the game is going to be infinite return -1 or return the end index.

From example

A = [3,4,2,2,7]
X = 4
S=2

we are at index 2, A[2] = 2; move is odd 2+1=3 exists at index 0 Array will become this
3,4,6,2,7
Now we are at index 0, make a jump because 4 exists on right (even move)

7,4,6,2,7
Now at index 1 4+1 5 doesnt exist on the right of 5

Answer is 1 final index.

A = [2,1]
X = 2
S = 1

'''

import bisect

# TC: O(n log n) in worst case due to list remove and insert operations in hashmap, O(log n) for bisect operations
# SC: O(n) for hashmap and visited set
class Solution:
    def jumpUpdate(self, arr, s, x):

        direction = 0  # 0 = Left (Odd move), 1 = Right (Even move)
        
        # HashMap banana index track karne ke liye
        hm = {}
        for i, val in enumerate(arr):
            if val not in hm:
                hm[val] = []
            hm[val].append(i)
            
        # Infinite loop check karne ke liye set
        # State format: (current_index, current_direction)
        visited = set()
        
        while True:
            # Agar hum is state par pehle bhi aa chuke hain -> Infinite Loop!
            state = (s, direction)
            if state in visited:
                return -1
            visited.add(state)
            
            target_val = arr[s] + 1
            
            # Agar target value poore array mein kahin nahi hai, toh game over
            if target_val not in hm or not hm[target_val]:
                return s
            
            pos_indices = hm[target_val]
            next_s = -1
            
            if direction == 0:  # LEFT MOVE
                # s se theek chota index dhoondna hai left side mein
                idx = bisect.bisect_left(pos_indices, s)
                if idx > 0:
                    next_s = pos_indices[idx - 1] # S se chota sabse pehla index
            else:  # RIGHT MOVE
                # s se theek bada index dhoondna hai right side mein
                idx = bisect.bisect_right(pos_indices, s)
                if idx < len(pos_indices):
                    next_s = pos_indices[idx] # S se bada sabse pehla index
                    
            # Agar valid jump nahi mili, toh game over
            if next_s == -1:
                return s
                
            # --- UPDATE STATE & HASHMAP ---
            old_s = s
            old_val = arr[old_s]
            
            # 1. Purani position se purani value remove karo HashMap se
            hm[old_val].remove(old_s)

            # agar us value ke liye koi aur index nahi bacha toh us key ko HashMap se hata do
            if len(hm[old_val]) == 0:
                del hm[old_val]
            
            # 2. Array ko update karo
            arr[old_s] += x
            new_val = arr[old_s]
            
            # 3. Nayi value ko HashMap mein sahi jagah insert karo (Sorted order maintain rakhne ke liye)
            if new_val not in hm:
                hm[new_val] = []

            bisect.insort(hm[new_val], old_s)
            
            # 4. Agle step par jao
            s = next_s
            direction = 1 - direction  # Toggle direction (0 -> 1, 1 -> 0)


print(Solution().jumpUpdate([3, 4, 2, 2, 7], 2, 4))  # Expected Output: 1
print(Solution().jumpUpdate([2, 1], 1, 2))  # Expected Output: 1 (kyunki 1+1=2 index 0 par hai jo left mein hai, par move even chahiye thi right ke liye, toh jump nahi hogi)