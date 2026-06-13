class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:

        n = len(words)

        # Step 1: Precompute overlaps (kitna part overlap ho raha hai)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    len_i, len_j = len(words[i]), len(words[j])
                    for k in range(min(len_i, len_j), 0, -1):
                        if words[i][len_i - k:] == words[j][:k]:
                            overlap[i][j] = k
                            break

        # dp[mask][i] store karega string ki MINIMUM length 
        # jab 'mask' waale words use ho chuke hain aur aakhiri word index 'i' hai.
        # Shuruat me sabko infinity (float('inf')) se initialize karenge.
        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]

        # Base case: Jab mask me sirf ek hi word ho, toh length us single word ke barabar hogi
        for i in range(n):
            dp[1 << i][i] = len(words[i]) # Mask me sirf 'i' waala word hai, toh length usi word ke barabar hogi

        # Step 2: DP State Transitions
        for mask in range(1 << n): # 2^n possible subsets of words

            for bit in range(n): # Jo word 'bit' hai, woh mask me hona chahiye tabhi aage badhenge

                if not (mask & (1 << bit)): # Agar 'bit' waala word mask me nahi hai, toh is state ko skip karo
                    continue

                # Agar yeh mask valid hai, toh yahan se agle word 'next_bit' par jaane ki koshish karo

                for next_bit in range(n): # Jo next word hai, woh bhi mask me nahi hona chahiye

                    if mask & (1 << next_bit): # Agar 'next_bit' waala word mask me pehle se hai, toh is par nahi ja sakte
                        continue
                        
                    next_mask = mask | (1 << next_bit) # Naye word ko mask me add karna

                    # nayi length = purani length + naye word ki length - overlap
                    new_len = dp[mask][bit] + len(words[next_bit]) - overlap[bit][next_bit]
                    
                    if new_len < dp[next_mask][next_bit]:
                        dp[next_mask][next_bit] = new_len
                        parent[next_mask][next_bit] = bit

        # Step 3: Best ending word dhoondo jisse overall length sabse kam ho
        full_mask = (1 << n) - 1
        min_len = float('inf')
        last_word_idx = -1

        # Full mask me sabhi words use ho chuke hain, toh aise ending word dhoondo jisse length minimum ho
        for i in range(n):
            if dp[full_mask][i] < min_len:
                min_len = dp[full_mask][i]
                last_word_idx = i

        path = []
        curr_mask = full_mask
        curr_word = last_word_idx

        # Step 4: Backtrack karke path nikaalo jisme words ka sequence hai
        while curr_word != -1:
            path.append(curr_word)
            next_word = parent[curr_mask][curr_word]
            curr_mask = curr_mask ^ (1 << curr_word) # reduce the mask by removing the current word
            curr_word = next_word

        path.reverse() # Taaki sahi sequence (start to end) mile

        # Step 5: Final Superstring construct karna
        result = words[path[0]]
        for i in range(1, len(path)):
            u, v = path[i-1], path[i]
            ol = overlap[u][v]
            result += words[v][ol:] # Overlap waale part ko chhod kar baaki add karo

        return result


print(Solution().shortestSuperstring(["abc", "cde", "def"])) # Output: "abcdef"
# dp: [[inf, inf, inf], [3, inf, inf], [inf, 3, inf], [6, 5, inf], [inf, inf, 3], [6, inf, 6], [inf, 6, 4], [7, 8, 6]]

print(Solution().shortestSuperstring(["alex","loves","leetcode"]))
print(Solution().shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"]))