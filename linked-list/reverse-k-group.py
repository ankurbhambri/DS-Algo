'''
Reverse Nodes in k-Group

Description: Given a singly linked list, reverse nodes in groups of k.

    Example:

    Input: 1 → 2 → 3 → 4 → 5, k = 2
    Output: 2 → 1 → 4 → 3 → 5

    Input: 1 → 2 → 3 → 4 → 5, k = 3
    Output: 3 → 2 → 1 → 5 → 4

    Input: 1 → 2 → 3 → 4 → 5 → 6, k = 3
    Output: 3 → 2 → 1 → 6 → 5 → 4

'''

class Node:
    def __init__(self, val=0, nxt = None):
        self.val = val
        self.nxt = nxt

class Solution:
    def reverseGroups(self, head, k):

        # helper function - get the kth node
        def getKthNode(curr_node, k_boubndary):
            while curr_node and curr_node.nxt and k_boubndary > 0:
                curr_node = curr_node.nxt
                k_boubndary -= 1
            return curr_node

        dummy = Node(0)
        dummy.nxt = head
        group_prev = dummy
        
        while True:

            kth_node = getKthNode(group_prev, k)
            if not kth_node or not kth_node.nxt:
                # group_prev.nxt = kth_node 
                break

            group_next = kth_node.nxt

            prev, curr = group_next, group_prev.nxt

            # reverse logic
            while curr != group_next:
                nxt = curr.nxt
                curr.nxt = prev
                prev = curr
                curr = nxt
                
            # connect the reversed nodes
            tmp = group_prev.nxt
            group_prev.nxt = kth_node
            group_prev = tmp

        return dummy.nxt


obj = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
head = Solution().reverseGroups(obj, 2)
while head:
    print(head.val)
    head = head.nxt

obj = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
head = Solution().reverseGroups(obj, 3)
while head:
    print(head.val)
    head = head.nxt

obj = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
head = Solution().reverseGroups(obj, 3)
while head:
    print(head.val)
    head = head.nxt

