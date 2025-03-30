# https://leetcode.com/problems/partition-labels

def partitionLabels(s):

    # Step 1: Find the last occurrence of each character
    last_occurrence = {c: i for i, c in enumerate(s)}

    # Step 2: Traverse and determine partitions
    partitions = []
    start, end = 0, 0

    for i, c in enumerate(s):
        end = max(end, last_occurrence[c])  # Expand partition to include current char's last occurrence
        
        if i == end:  # If we reached the end of the partition
            partitions.append(end - start + 1)
            start = i + 1  # Start new partition

    return partitions

print(partitionLabels("ababcbacadefegdehijhklij"))  # Output: [9, 7, 8]
print(partitionLabels("eccbbbbdec"))  # Output: [10]
print(partitionLabels("ababcdefcjh"))  # Output: [4,5,1,1]
