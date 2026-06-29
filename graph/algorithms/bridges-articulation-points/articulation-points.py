########## Tarjan's Algorithm to find articulation points in a graph ##########

from collections import defaultdict

# TC: O(V + E), SC: O(V + E)
class Solution:
    def articulationPoints(self, V, edges):

        graph = defaultdict(list)

        # Undirected graph banao
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # disc[node] = node pehli baar kis time visit hua
        disc = [-1] * V

        # low[node] = meri subtree sabse purane kis node tak pahunch sakti hai
        low = [-1] * V

        # Batayega kaun-kaun articulation point hai
        isAP = [False] * V

        timer = 0

        def dfs(node, parent):

            nonlocal timer

            # Discovery aur low dono initially same hote hain
            disc[node] = low[node] = timer
            timer += 1

            # Sirf root node ke liye useful hai
            children = 0

            for nei in graph[node]:

                # Parent wali edge ko ignore karo
                if nei == parent:
                    continue

                # Agar neighbor abhi tak visit nahi hua to DFS lagao
                if disc[nei] == -1:

                    children += 1

                    dfs(nei, node)

                    # DFS se wapas aane ke baad child ka low value propagate karo
                    low[node] = min(low[node], low[nei])

                    # Root node agar 2 ya usse jyada DFS children banata hai,
                    # to root hataane par graph disconnect ho jayega.
                    if parent == -1 and children > 1:
                        isAP[node] = True

                    # Agar child ki subtree node ke ancestors tak
                    # kisi aur path se nahi pahunch sakti,
                    # to node articulation point hai.
                    if parent != -1 and low[nei] >= disc[node]:
                        isAP[node] = True

                # Neighbor already visit ho chuka hai aur parent bhi nahi hai,
                # iska matlab ye back-edge hai.
                # Is back-edge ki wajah se hum kisi purane node tak pahunch sakte hain.
                else:
                    low[node] = min(low[node], disc[nei])

        # Graph disconnected bhi ho sakta hai,
        # isliye har component se DFS start karo
        for i in range(V):
            if disc[i] == -1:
                dfs(i, -1)

        ans = []

        for i in range(V):
            if isAP[i]:
                ans.append(i)

        return ans