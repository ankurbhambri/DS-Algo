# https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import randint

class RandomizedSet:

    def __init__(self):
        self.hm = {}
        self.arr = []        

    def insert(self, val: int) -> bool:
        if val not in self.hm:
            self.hm[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:

        if val in self.hm:

            idx = self.hm[val]

            lv = self.arr[-1]

            self.arr[idx] = lv

            self.hm[lv] = idx

            del self.hm[val]
            self.arr.pop()

            return True

        return False

    def getRandom(self) -> int:
        index = randint(0, len(self.arr) - 1)
        return self.arr[index]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(3)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
