def getMilestoneDays(revenues, milestones):
    ps = revenues
    for i in range(1, len(revenues)):
        ps[i] = ps[i - 1] + revenues[i]

    res = []

    for mile in milestones:

        l, r = 0, len(revenues) - 1

        while l < r:

            m = (l + r) // 2

            if ps[m] < mile:
                l = m + 1
            else:
                r = m

        res.append(l + 1)

    return res


revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
print(getMilestoneDays(revenues, milestones))
