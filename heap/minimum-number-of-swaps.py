'''
Finding the minimum number of swaps needed to reach a state where no element in the fileSize array matches the element at the same index in the affinity array.

Objective: Rearrange fileSize so that for all $i$, $fileSize[i] != affinity[i] and we want the minimum number of swaps.

If it's impossible (e.g., more than half the files have the same value and the affinities also match that value excessively), return -1.

'''

import heapq
from collections import Counter

def getMinSwaps(fileSize, affinity):

    n = len(fileSize)
    bad_indices = []

    # 1. Identify indices where fileSize matches affinity (i.e., "bad" positions)
    for i in range(n):
        if fileSize[i] == affinity[i]:
            bad_indices.append(i)

    if not bad_indices:
        return 0

    # 2. Count frequencies of the 'bad' values
    bad_values = [fileSize[i] for i in bad_indices]
    counts = Counter(bad_values)

    # Max-Heap stores (-frequency, value) aka Priority Queue
    max_heap = [[-count, val] for val, count in counts.items()]
    heapq.heapify(max_heap)

    total_swaps = 0

    # 3. Phase 1: Destroy "bad" counts by pairing them together
    while len(max_heap) > 1:

        c1, v1 = heapq.heappop(max_heap)
        c2, v2 = heapq.heappop(max_heap)

        # We perform one swap to fix one of v1 and one of v2
        total_swaps += 1

        if c1 + 1 < 0:
            heapq.heappush(max_heap, [c1 + 1, v1])
        if c2 + 1 < 0:
            heapq.heappush(max_heap, [c2 + 1, v2])

    # 4. Phase 2: Handle remaining bad values of the same type
    if not max_heap:
        return total_swaps

    remainder_count, remainder_val = -max_heap[0][0], max_heap[0][1]

    # We need to swap each remaining 'bad' element with a 'good' bond.
    # A 'good' bond is index j where:
    # fileSize[j] != remainder_val AND affinity[j] != remainder_val

    available_good_slots = 0
    for i in range(n):
        # Index i is 'good' if it wasn't a match initially
        if fileSize[i] != affinity[i]:
            # It's a safe swap target only if it's not the remainder value 
            # and the affinity there isn't the remainder value
            if fileSize[i] != remainder_val and affinity[i] != remainder_val:
                available_good_slots += 1

    if available_good_slots >= remainder_count:
        return total_swaps + remainder_count

    return -1

# Example Test
fileSize = [2, 2, 1, 1, 2]
affinity = [2, 1, 1, 1, 2]
print(f"Minimum swaps needed: {getMinSwaps(fileSize, affinity)}")