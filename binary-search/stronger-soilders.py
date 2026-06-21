'''
    You have an army of normal soilders, you can upgrade a soilder to be stronger by feeding him X magical apples
    Initially, you have M magical apples. You can buy extra magical (from the Iron Bank!)
    You selling one of your soilders for Y magical apples.

    Calculate what is the maximum number of stronger soilders you can have?

    Input:

    N   M   X   Y
    5   10  2   2 -> 5 soilders
    3   10  4   2 -> 2 soilders
    5   1   2   3 -> 1 soilders
'''

# Binary search
def stronger_soilders(N, M, X, Y):

    l = 0
    h = N
    ans = 0

    while l <= h:

        mid = (l + h) // 2  # mid represents target strong soldiers

        # Calculate the number of magical apples needed to upgrade mid soldiers
        needed = mid * X

        # Calculate the number of magical apples available after selling (N - mid) soldiers
        available = M + (N - mid) * Y
        
        if needed <= available:
            ans = mid
            l = mid + 1
        else:
            h = mid - 1

    return ans

print(stronger_soilders(5, 10, 2, 2)) # 5
print(stronger_soilders(3, 10, 4, 2)) # 2
