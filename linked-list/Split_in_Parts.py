# https://leetcode.com/problems/split-linked-list-in-parts/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def splitListToParts(head, k):

    # Step 1: Calculate the total number of nodes in the linked list
    curr = head
    total_nodes = 0

    while curr:
        total_nodes += 1
        curr = curr.next

    # Step 2: Determine the size of each part and the remainder
    part_size = total_nodes // k
    extra_nodes = (
        total_nodes % k
    )  # These will be distributed across the first 'extra_nodes' parts

    result = []

    curr = head
    for i in range(k):
        # For each part, start at the current node (or None if the list is exhausted)
        part_head = curr

        # Determine the correct size of this part (part_size + 1 for the first extra_nodes parts)
        current_part_size = part_size + (1 if i < extra_nodes else 0)

        # Traverse the part and detach it from the rest of the list
        for j in range(current_part_size - 1):
            if curr:
                curr = curr.next

        # Detach the current part from the rest of the list
        if curr:
            next_part = curr.next
            curr.next = None
            curr = next_part

        # Add this part (or None) to the result list
        result.append(part_head)

    return result


nodes1 = ListNode(1, ListNode(2, ListNode(3)))
print(splitListToParts(nodes1, 5))  # [[1],[2],[3],[],[]]

nodes2 = ListNode(
    1,
    ListNode(
        2,
        ListNode(
            3,
            ListNode(
                4,
                ListNode(
                    5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))
                ),
            ),
        ),
    ),
)
print(splitListToParts(nodes2, 3))  # [[1,2,3,4],[5,6,7],[8,9,10]]
