# simple structure of tak/not take values from subsequences


def func(arr):

    n = len(arr)

    def helper(i, res):

        if i == n:
            print(res)
            return

        # take
        res.append(arr[i])
        helper(i + 1, res)

        # not take (backtrack)
        res.remove(arr[i])
        helper(i + 1, res)

    return helper(0, [])


func([3, 1, 2])

"""
o/p:  [3, 1, 2]
      [3, 1]
      [3, 2]
      [3]
      [1, 2]
      [1]
      [2]
      []
"""
