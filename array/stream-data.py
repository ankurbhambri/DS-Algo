"""

We have stream of integers coming to your function. 
The function should generate continuous output stream which computes sum of last 5 elements.

Input Stream -> 3,4,2,5,3,6,1,7,4..

Output stream - 17, 20, 17, 22, 21..

Idea - here is to use prefix sum queue to append and remove from the rear and append from front

"""


class Iterator:

    def __init__(self, val):
        self.val = val

    def get_next(self):
        return self.val


class Solution:

    def __init__(self, size):
        self.size = size
        self.q = []

    def insert_iterator(self, iterator_val):

        if self.q:
            if len(self.q) == self.size:
                a = self.q[0][0]
                self.q.append((iterator_val, self.q[-1][1] + iterator_val - a))
                self.q.pop(0)
            else:
                self.q.append((iterator_val, self.q[-1][1] + iterator_val))
        else:
            self.q.append((iterator_val, iterator_val))

    def output_iterator(self):
        if len(self.q) == self.size:
            return self.q[-1]
        return None


# 3,4,2,5,3,6,1,7,4

obj1 = Solution(5)


def calling_function(iter_val):
    obj1.insert_iterator(iter_val)
    if len(obj1.q) == obj1.size:
        print(obj1.output_iterator()[1])


obj = Iterator(3)
calling_function(obj.get_next())
obj = Iterator(4)
calling_function(obj.get_next())
obj = Iterator(2)
calling_function(obj.get_next())
obj = Iterator(5)
calling_function(obj.get_next())
obj = Iterator(3)
calling_function(obj.get_next())
obj = Iterator(6)
calling_function(obj.get_next())
obj = Iterator(1)
calling_function(obj.get_next())
obj = Iterator(7)
calling_function(obj.get_next())
obj = Iterator(4)
calling_function(obj.get_next())
