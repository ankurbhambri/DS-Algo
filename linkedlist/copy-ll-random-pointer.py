# https://leetcode.com/problems/copy-list-with-random-pointer/description/

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None

    # 1. Clone each node and insert it right after the original node
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next, None)
        curr.next = new_node
        curr = new_node.next

    # 2. Assign random pointers to the cloned nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # 3. Separate the cloned list from the original
    curr = head
    cloned_head = head.next
    while curr:
        cloned_node = curr.next
        curr.next = cloned_node.next
        if cloned_node.next:
            cloned_node.next = cloned_node.next.next
        curr = curr.next

    return cloned_head

# Node1 -> Node2 -> Node3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# Random pointers:
node1.random = node3   # 1 → 3
node2.random = node1   # 2 → 1
node3.random = node3   # 3 → 3

print("Original list:")
print_list(node1)

# Clone
cloned_head = copyRandomList(node1)

print("\nCloned list:")
print_list(cloned_head)
