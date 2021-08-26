class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # head is default NULL
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.isempty():
            return None

        else:
            # Removes the head node and makes
            # the preceeding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    # Returns the head node data
    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    # Prints out the stack
    def display(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:

            while iternode != None:

                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            return

    def reverse(self):

        prev = None

        while self.head:
            next = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next

        self.head = prev

        return self.head


# Driver code
stack_obj = Stack()

stack_obj.push(11)
stack_obj.push(22)
stack_obj.push(33)
stack_obj.push(44)

# Display stack elements
stack_obj.display()


stack_obj.reverse()
print("\nReverse stack ")

stack_obj.display()

# Print top element of stack
print("\nTop element is ", stack_obj.peek())

# Delete top elements of stack
stack_obj.pop()
stack_obj.pop()

# Display stack elements
stack_obj.display()

# Print top element of stack
print("\nTop element is ", stack_obj.peek())

# This code is contributed by Mathew George
