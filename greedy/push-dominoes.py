# https://leetcode.com/problems/push-dominoes

from collections import deque

def pushDominoes(dominoes):

    dom = list(dominoes)
    q = deque()

    for i, d in enumerate(dom):
        if d != '.':
            q.append((i, d))
    
    while q:
        i, d = q.popleft()
        
        if d == 'L' and i > 0 and dom[i - 1] == '.':
            q.append((i - 1, 'L'))
            dom[i - 1] = 'L'
            
        elif d == 'R':
            if i + 1 < len(dom) and dom[i + 1] == '.':
                # means next to next is L leaning we have to pop it
                if i + 2 < len(dom) and dom[i  + 2] == 'L':
                    q.popleft()
                else:
                    q.append((i + 1, 'R'))
                    dom[i + 1] = 'R'

    return ''.join(dom)

print(pushDominoes("RR.L"))  # Output: "RR.L"
print(pushDominoes(".L.R...LR..L.."))  # Output: "LL.RR.LLRRLL.."