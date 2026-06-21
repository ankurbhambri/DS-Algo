"""
You are enjoying your vacation and suddenly you are informed to reach the workplace.

You are given a root map in form of tree rooted at 1.

There are total N stations numbered from 1 to N in form of nodes.

You are at station X away from workpalce at Y. Now, to reach from X to Y, you are provided with two nodes of transport.

You move from station A to station B, provided the 2 facilities.

    - If station A and B are on same level of the tree, the cost incurred for the transport is 0.

    - Else the cost will be sum of the values of nodes, given both the nodes are connected by an edge, i.e A + B

You have to reach back to your workplace spending minimum cost.

You are given Q independent queries to be answered where X, Y are the inputs to you queries.

7 nodes:
         1
      //   \\
      2      3
   // || \\   \\
  7  4    6     5

Query: 1 -> 7

paths = 1 -> 2 -> 7 - (3 + 9) = 12

paths = 1 -> 3 -> 5 - > 7 - (4 + 8) = 12

paths = 1 -> 2 -> 4 - (3 + 6) = 9


########################### Approach Explanation ###########################  


### Hamara Tree Structure:

- Root (Level 0): 1
- Level 1: 2, 3
- Level 2: 7, 4, 6, 5

---

### Step 1: Level Pata Karna

Sabse pehle BFS ka code har node ka Level (depth) nikalta hai aur unhe yaad rakh leta hai:

- level[1] = 0
- level[2] = 1, level[3] = 1
- level[7] = 2, level[4] = 2, level[6] = 2, level[5] = 2

Yahan tak max_level = 2 ho chuka hai.

---

### Step 2: Minimum Transition Cost (Sabse sasti sidhi dhoodna)

Ab code har ek edge (raaste) ko check karega aur dekhega ki ek level se dusre level jaane ka sabse sasta raasta kaun sa hai.

Shuru mein min_edge_cost = float('inf') se initialize karta hai, matlab abhi tak koi raasta nahi mila.

Ab loop chalega saare edges par:

1. Edge (1, 2):
- Levels: 1 (Level 0) aur 2 (Level 1). Chhota level kaun sa hai? 0.
- Cost: 1 + 2 = 3.
- min_edge_cost[0] ban gaya 3.


2. Edge (1, 3):
- Levels: 1 (Level 0) aur 3 (Level 1). Chhota level: 0.
- Cost: 1 + 3 = 4.
- Kya 4 chhota hai pehle wale 3 se? Nahi. To min_edge_cost[0] 3 hi rahega.


3. Edge (2, 7):
- Levels: 2 (Level 1) aur 7 (Level 2). Chhota level: 1.
- Cost: 2 + 7 = 9.
- min_edge_cost[1] ban gaya 9.


4. Edge (2, 4):
- Levels: 2 (Level 1) aur 4 (Level 2). Chhota level: 1.
- Cost: 2 + 4 = 6.
- Kya 6 chhota hai pehle wale 9 se? Haan! To min_edge_cost[1] ab update hokar 6 ho gaya.


5. Edge (2, 6): Cost 2+6=8 (6 se bada hai, ignore).
6. Edge (3, 5): Cost 3+5=8 (6 se bada hai, ignore).

- Step 2, ke baad hamara result:

- min_edge_cost[0] (Lvl 0 -> Lvl 1 ka sasta raasta) = 3

- min_edge_cost[1] (Lvl 1 -> Lvl 2 ka sasta raasta) = 6

---

### Step 3: Prefix Sum Array (Kharcha jorhte jana)

Ab hum shuruat se lekar aage tak ka total kharcha jorhte hain taaki baad mein baar-baar plus na karna pade.

- prefix_sum[0] = 0 (Level 0 par hi rehne ka kharcha)

- prefix_sum[1] = prefix_sum[0] + min_edge_cost[0] -> 0 + 3 = 3 (Level 0 se Level 1 tak aane ka total kharcha)

- prefix_sum[2] = prefix_sum[1] + min_edge_cost[1] -> 3 + 6 = 9 (Level 1 se Level 2 tak aane ka total kharcha)

Hamara final prefix_sum array taiyar hai: [0, 3, 9]

---

### Step 4: Queries Solve Karna (Asli Jadu)

Query A: 1 se 7 tak jana hai

1. Code check karega: 1 ka level kya hai? 0 (root node). 7 ka level kya hai? 2.
2. Dono alag level par hain? Haan.
3. Code formula lagayega: prefix_sum[high_lvl] -> prefix_sum[low_lvl] - prefix_sum[2] = prefix_sum[0] - 9 - 0 = 9
4. Answer: 9 (Wahi jo humne manually nikala tha: 1 -> 2 -> 4 aur fir free mein 4 -> 7).

#### Query B: 3 se 7 tak jana hai

1. Code check karega: 3 ka level kya hai? 1. 7 ka level kya hai? 2.
2. Dono alag level par hain? Haan.
3. Code formula lagayega: prefix_sum[2] - prefix_sum[1] = 9 - 3 = 6
4. Answer: 6 (Wahi jo humne nikala tha: free mein 3 -> 2, fir niche 2 -> 4 cost 6, fir free mein 4 -> 7).

"""

from collections import defaultdict, deque

# TC: O(N + Q), O(N) to visit all nodes and edges, Prefix Sum Setup: O(L) where L is the max depth of the tree (L <= N).
# SC: O(N) for adjacency list, level mapping, and prefix sum array.
class Solution:
    def vacation(self, edges, queries):

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        level = {}
        level_nodes = defaultdict(list)

        queue = deque([1])
        level[1] = 0
        level_nodes[0].append(1)

        max_level = 0

        # Step 1: Level find karna using BFS
        while queue:

            curr = queue.popleft()
            curr_level = level[curr]
            max_level = max(max_level, curr_level)

            for neighbor in adj[curr]:
                if neighbor not in level:
                    level[neighbor] = curr_level + 1
                    level_nodes[curr_level + 1].append(neighbor)
                    queue.append(neighbor)

        # Step 2: Minimum transition cost find karna, level i se level i+1 ke liye sabse sasta raasta dhoodna
        min_edge_cost = [float('inf')] * max_level

        for u, v in edges:

            lvl_u = level[u]
            lvl_v = level[v]

            # An edge always connects level i and level i+1
            from_lvl = min(lvl_u, lvl_v)

            edge_cost = u + v

            # yeh check isliye hai kyunki agar dono nodes same level par hain, to cost 0 hai, aur hum sirf level transition ke liye cost chahte hain
            # if from_lvl < max_level:
            min_edge_cost[from_lvl] = min(min_edge_cost[from_lvl], edge_cost)

        # Step 3: Build a prefix sum array of level transition costs for O(1) query lookup
        prefix_sum = [0] * (max_level + 1)
        for i in range(max_level):
            prefix_sum[i + 1] = prefix_sum[i] + min_edge_cost[i]

        # Step 4: Finally!! Answer the queries
        results = []
        for X, Y in queries:

            lvl_x = level[X]
            lvl_y = level[Y]

            if lvl_x == lvl_y:
                results.append(0)

            else:
                # The cost is the sum of the minimum edges between the two levels
                low_lvl = min(lvl_x, lvl_y)
                high_lvl = max(lvl_x, lvl_y)
                cost = prefix_sum[high_lvl] - prefix_sum[low_lvl]
                results.append(cost)

        return results


print(Solution().vacation(edges=[(1,2),(1,3),(2,7),(2,4),(2,6),(3,5)], queries=[(1, 7), (3, 7)]))  # [9, 6]