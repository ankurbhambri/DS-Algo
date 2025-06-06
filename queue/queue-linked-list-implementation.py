# Node class for Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Queue class using Linked List
class Queue:
    def __init__(self):
        self.head = None  # Points to front
        self.tail = None  # Points to rear

    # Enqueue operation - add to tail (rear)
    def enqueue(self, val):
        new_node = Node(val)

        if self.tail:
            self.tail.next = new_node  # Link new node after tail
        self.tail = new_node  # Update tail to new node

        if not self.head:
            self.head = new_node  # If empty, head = tail

    # Dequeue operation - remove from head (front)
    def dequeue(self):
        
        if not self.head:
            return "Queue is empty"

        val = self.head.val
        self.head = self.head.next  # Move head to next node

        if not self.head:
            self.tail = None  # Queue is now empty

        return val

    # Peek at front element
    def peek(self):

        if not self.head:
            return "Queue is empty"
        
        return self.head.val

    # Check if queue is empty
    def isEmpty(self):
        return self.head is None

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  # 10
print(q.peek())     # 20
print(q.isEmpty())  # False
q.dequeue()
print(q.isEmpty())  # True
