# https://leetcode.com/problems/cycle-length-queries-in-a-tree/description/


# TC: O(Q * logN) where Q is the number of queries and N is the number of nodes in the tree
# SC: O(1) for extra space (excluding the output list)
class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        ans = []
        
        for a, b in queries:
            jumps = 0
            
            # Jab tak dono nodes kisi ek common ancestor (LCA) par nahi milte
            while a != b:
                if a > b:
                    a //= 2  # A bada hai, toh A ko uske parent par bhejo
                else:
                    b //= 2  # B bada hai, toh B ko uske parent par bhejo
                jumps += 1   # Ek edge cover ho gayi
            
            # Total Cycle = Jo edge humne jodi (1) + Tree ke andar ke jumps
            ans.append(jumps + 1)
            
        return ans


# Binary lifting approach for LCA (Lowest Common Ancestor) in a tree

import math

class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        
        # 1. Depth nikalne ka function (using log2)
        def get_depth(u: int) -> int:
            return int(math.log2(u))
            
        # 2. k-th ancestor nikalne ka function (using Right Shift)
        def get_kth_ancestor(u: int, k: int) -> int:
            return u >> k

        # 3. Binary Search se LCA nikalne ka function
        def get_lca(u: int, v: int) -> int:
            depth_u = get_depth(u)
            depth_v = get_depth(v)
            
            # Hamesha v ko gahra (deeper) rakhein
            if depth_u > depth_v:
                u, v = v, u
                depth_u, depth_v = depth_v, depth_u
                
            # Dono ko same depth par lao
            diff = depth_v - depth_u
            v = get_kth_ancestor(v, diff)
            
            if u == v:
                return u
                
            # Binary Search se dhoondo ki kitne jumps tak dono alag rehte hain
            l, r = 0, 31
            while l < r:
                mid = (l + r + 1) // 2
                new_u = u >> mid
                new_v = v >> mid
                
                if new_u == new_v:
                    r = mid - 1  # LCA ke upar ya LCA par hain, toh niche aao
                else:
                    l = mid      # Abhi bhi niche hain, toh aur upar jao
                    
            # 'l' tak dono alag the, toh 'l' steps upar le jakar uska ek aur parent (>> 1) le lo
            return (u >> l) >> 1

        # 4. Saari queries process karein
        ans = []
        for a, b in queries:
            lca = get_lca(a, b)
            
            # Formula: depth(a) + depth(b) - 2 * depth(LCA)
            path_len = get_depth(a) + get_depth(b) - 2 * get_depth(lca)
            
            # Total Cycle = New Edge (1) + Path Length
            ans.append(1 + path_len)
            
        return ans