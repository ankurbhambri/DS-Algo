# https://leetcode.com/problems/frog-jump/


def canCross(stones):

    # We will keep track of the k jumps that frog took to reach that stone
    hm = {i: set() for i in stones}

    # First stone always has 1 jump
    hm[stones[0]].add(1)

    for i in range(len(stones)):

        currStone = stones[i]

        # Taking all the jumps for the curr stone
        jumpOptions = hm[currStone]

        for j in jumpOptions:

            # Searching if the position w.r.t is leading to another stone or last stone
            pos = currStone + j

            if pos == stones[-1]:
                return True

            # If it reaches any stone in stone array
            if pos in hm:

                # Checking whether jump j - 1 is not lte 0
                # And, putting all jumps that frog can take to reach and keep distinct in the set of that stone.
                if j - 1 > 0:
                    hm[pos].add(j - 1)
                hm[pos].add(j)
                hm[pos].add(j + 1)

    return False
