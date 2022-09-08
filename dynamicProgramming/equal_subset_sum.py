def equal_sum_recursive(arr):

    if sum(arr) % 2 != 0:
        return False

    def helper(n, W):

        # Base Cases
        if W == 0:
            return True

        elif n == 0:
            return False

        else:
            item = arr[n - 1]
            if item <= W:
                c1 = helper(n - 1, W - item)
                c2 = helper(n - 1, W)
                return c1 or c2
            else:
                return helper(n - 1, W)

    return helper(len(arr), sum(arr) // 2)


def equal_sum_cache(arr):

    cache = {}

    if sum(arr) % 2 != 0:
        return False

    def helper(n, W):

        # Base Cases
        if W == 0:
            return True

        elif n == 0:
            return False
        
        elif (n, W) in cache:
            return cache[(n, W)]

        else:
            item = arr[n - 1]
            if item <= W:
                c1 = helper(n - 1, W - item)
                c2 = helper(n - 1, W)
                c = c1 or c2
            else:
                c = helper(n - 1, W)
            cache[(n, W)] = c
            return c

    return helper(len(arr), sum(arr) // 2)    
    
if __name__ == "__main__":

    arr = [1, 5, 11, 5]
    print(equal_sum_recursive(arr))
    print(equal_sum_cache(arr))

