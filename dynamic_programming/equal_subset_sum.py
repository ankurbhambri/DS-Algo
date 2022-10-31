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


def equal_sum_memo(nums):

    if sum(nums) % 2 != 0:
        return False
    
    dp = set()
    dp.add(0)
    
    val = sum(nums) // 2

    for i in range(len(nums) - 1, -1, -1):
        nextDp = set()
        for t in dp:
            nextDp.add(t + nums[i])
            nextDp.add(t)
            
        dp = nextDp
        
    return True if val in dp else False   
    
if __name__ == "__main__":

    arr = [1, 5, 11, 5]
    print(equal_sum_recursive(arr))
    print(equal_sum_memo(arr))

