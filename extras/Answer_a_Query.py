from bisect import bisect_right
from sortedcontainers import SortedList


def answerQueries(queries, N):
    result = []
    true_indices = SortedList()

    for q_type, index in queries:

        if q_type == 1:
            # SET query: set index to true
            if index not in true_indices:
                true_indices.add(index)
        elif q_type == 2:
            # GET query: find nearest true to the right of index
            pos = bisect_right(true_indices, index - 1)
            if pos < len(true_indices):
                result.append(true_indices[pos])
            else:
                result.append(-1)

    return result


print(answerQueries([[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]], 5))
