# https://leetcode.com/problems/subsets/submissions/
# https://leetcode.com/problems/subsets-ii/


def power_set(elements):
    n = len(elements)
    power_set_size = 2**n
    power_set_result = []
    # seen = set()
    for i in range(power_set_size):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(elements[j])

        # for top 2 question please enalbe this
        # subset.sort()
        # if tuple(subset) not in seen:
        #     power_set_result.append(subset)
        #     seen.add(tuple(subset))
        power_set_result.append(subset)

    return power_set_result


elements = [1, 2, 3]
print(power_set(elements))
