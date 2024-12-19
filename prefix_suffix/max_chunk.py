# https://leetcode.com/problems/max-chunks-to-make-sorted/description/


def maxChunksToSorted(arr):

    n = len(arr)
    chunks = 0
    max_element = 0

    for i in range(n):

        max_element = max(max_element, arr[i])

        if max_element == i:
            # All values in range [0, i] belong to the prefix arr[0:i]; a chunk can be formed
            chunks += 1

    return chunks


maxChunksToSorted([1, 0, 2, 3, 4])  # 4
maxChunksToSorted([4, 3, 2, 1, 0])  # 1
maxChunksToSorted([2, 0, 1, 3])  # 2
maxChunksToSorted([0, 1, 2, 3, 4])  # 5
maxChunksToSorted([1, 2, 0, 3])  # 2
maxChunksToSorted([1, 0, 3, 2])  # 2
