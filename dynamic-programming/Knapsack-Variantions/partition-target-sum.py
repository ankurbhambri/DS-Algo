"""https://practice.geeksforgeeks.org/problems/target-sum-1626326450/1

p1 partition of +ve numbers
p2 partition fd -ve numbers


cndts: p1 - p2 = target, p1 + p2 = sum(arr)

equation :

let p1 = X

p2 = sum(arr) - x -------------- wrt p1 + p2 = sum(arr)


put val in this eq

p1 - p2 = target

x - sum(arr) + x = target

x = sum(arr) + target // 2  ------------- final eq will use in problem

x tends to p1 so we have to find number of x we can generate using p1 and 
this prblm converts into perfect sum prblm bcoz p1 is whole array and x is sum which
we have to find nos of times x can be genrated

image.png

"""


def target_sum(arr, target):
    x = sum(arr) + target
    n = len(arr)
    if x % 2 != 0:
        return 0
    else:
        x = x // 2
    arr.sort(reverse=True)
    memo = {}

    def helper(N, W):
        if N == 0:
            if W == 0:
                return 1
            return 0
        elif (N, W) in memo:
            return memo[(N, W)]
        else:
            item = arr[N - 1]
            if W >= item:
                c1 = helper(N - 1, W - item)
                c2 = helper(N - 1, W)
                c = c1 + c2
            else:
                c = helper(N - 1, W)
            memo[(N, W)] = c
            return c

    return helper(n, x)


print(target_sum([1, 1, 1, 1, 1], 3))
