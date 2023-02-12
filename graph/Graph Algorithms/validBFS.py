# problem link https://codeforces.com/problemset/problem/1037/D

from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
for i in range (n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
 
arr = list(map(int, input().split()))
reorder = [None] * (n + 1)

for i in range (n):
    reorder[arr[i]] = i

for i in range (n):
    graph[i].sort(key = lambda x : reorder[x])
res = [0 for i in range (n)]
 
q = deque([1])
visited = set([1])
res = []
while q:
    cur = q.popleft()
    res.append(cur)
    for nei in graph[cur]:
        if nei not in visited:
            visited.add(nei)
            q.append(nei)
        
flag = True
for i in range (n):
    if res[i] != arr[i]:
        flag = False
        break 
        
if flag:
    print("Yes")
else:
    print("No")
    
    
    
# -- another way out ---
# from collections import deque

# n = int(input())
# graph = [[] for i in range (n)]
# for i in range (n - 1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     graph[a].append(b)
#     graph[b].append(a)
 
# arr = list(map(int, input().split()))
# reorder = [None for i in range (n + 1)]
# for i in range (n):
#     arr[i] -= 1
#     reorder[arr[i]] = i
 
# for i in range (n):
#     graph[i].sort(key = lambda x : reorder[x])
# res = [0 for i in range (n)]
 
# q = deque([0])
# visited = [False for i in range (n)]
# visited[0] = True
# res = []
# while q:
#     cur = q.popleft()
#     res.append(cur)
#     for neighbor in graph[cur]:
#         if visited[neighbor] == False:
#             visited[neighbor] = True
#             q.append(neighbor)
        
# flag = True
# for i in range (n):
#     if res[i] != arr[i]:
#         flag = False
#         break 
        
# if flag:
#     print("Yes")
# else:
#     print("No")
    
