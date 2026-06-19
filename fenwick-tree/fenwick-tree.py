# https://cp-algorithms.com/data_structures/fenwick.html


# Fenwick Tree (Binary Indexed Tree)

'''
Update i += i & (-i): Isme hum Bottom-to-Top (Neeche se Upar) jaate hain. 
Hum chote child se shuru karke un sabhi bade Parents tak jaate hain jo us child par dependent hain, taaki sabka data naye badlav ke hisaab se update ho jaye.

Query i -= i & (-i): Isme hum Top-to-Bottom / Right-to-Left (Piche ki taraf) jaate hain. 
Hum bade pre-computed blocks se shuru karte hain aur unke piche wale Children/Sub-blocks par jump karte hain, taaki ready-made sums ko utha kar jaldi se total sum nikal sakein.

TC: O(log n) for both update and query operations
SC: O(n) for the tree array

'''

# Below code is for Point Update and Range Query
class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        self.bit = [0] * (size + 1)

    def update(self, i: int, delta: int):
        while i <= self.n:
            self.bit[i] += delta
            i += i & (-i)

    def query(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & (-i)
        return res

    def range_query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.query(r) - self.query(l - 1)


arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]

n = len(arr)

bit = FenwickTree(n)

for i in range(n):
    bit.update(i + 1, arr[i])

print(bit.range_query(2, 5))

bit.update(3, 3)  # update index 3 to 3

print(bit.range_query(2, 5))


# Below code is for Range Update and Point Query
# Will use difference array technique to convert range update to point update
class FenwickTreeRangeUpdate:
    def __init__(self, size: int):
        self.n = size
        self.bit = [0] * (size + 1)

    def update(self, i: int, delta: int):
        while i <= self.n:
            self.bit[i] += delta
            i += i & (-i)

    def range_update(self, l: int, r: int, delta: int):
        self.update(l, delta)
        self.update(r + 1, -delta)

    def query(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & (-i)
        return res

    def range_query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.query(r) - self.query(l - 1)

arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
n = len(arr)

bit_range_update = FenwickTreeRangeUpdate(n)

bit_range_update.range_update(3, 5, 2)  # Update indices 3 to 5 by adding 2

bit_range_update.range_update(1, 3, -1)  # Update indices 1 to 3 by subtracting 1

print(bit_range_update.query(3))  # Query the value at index 3

print(bit_range_update.range_query(2, 5))  # Query the sum from index 2 to 5