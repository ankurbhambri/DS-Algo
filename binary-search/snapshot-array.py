class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [[[0, 0]] for _ in range(length)]  # Initialize with (snap_id=0, val=0)
        self.snap_id = 0
    
    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])
    
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
    
    def get(self, index: int, snap_id: int) -> int:

        history = self.arr[index]
        left, right = 0, len(history) - 1
        result = 0
        
        # Binary search for largest snap_id <= target snap_id
        while left <= right:
            mid = (left + right) // 2
            if history[mid][0] <= snap_id:
                result = history[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result


obj = SnapshotArray(3) # [[[0, 0]], [[0, 0]], [[0, 0]]]

obj.set(0,5) # [[[0, 5]], [[0, 0]], [[0, 0]]]
obj.snap()

obj.set(0,6) # [[[0, 5], [1, 6]], [[0, 0]], [[0, 0]]]
obj.set(0,7) # [[[0, 5], [1, 7]], [[0, 0]], [[0, 0]]]
obj.set(1,2) # [[[0, 5], [1, 7]], [[0, 0], [1, 2]], [[0, 0]]]

obj.get(0,0)  # Output: 5
obj.get(0,1)  # Output: 7
obj.get(1,1)  # Output: 2
