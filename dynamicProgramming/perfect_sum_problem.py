# number of subset can be drived from array

def perfect_sum_recursive(arr):

    def helper(n, W):
        if W == 0:
            return 1
        elif n == 0:
            return 0
        else:
            item = arr[n - 1]
            if item <= W:
                c1 = helper(n - 1, W - item)
                c2 = helper(n - 1, W)
                return c1 + c2
            else:
                return helper(n - 1, W)
    return helper(len(arr), 10)


def perfect_sum_cache(arr):
    cache = {}
    mod = 10 ** 9 + 7
    def helper(n, W):
        if W == 0:
            return 1
        elif n == 0:
            return 0
        elif (n, W) in cache:
            return cache[(n, W)]
        else:
            item = arr[n - 1]
            if item <= W:
                c1 = helper(n - 1, W - item)
                c2 = helper(n - 1, W)
                c = (c1 % mod + c2 % mod) % mod
            else:
                c = helper(n - 1, W)
            cache[(n, W)] = c
            return c
    return helper(len(arr), 10)
if __name__ == "__main__":

    arr = [2, 3, 5, 6, 8, 10]
    print(perfect_sum_recursive(arr))
    print(perfect_sum_cache(arr))

