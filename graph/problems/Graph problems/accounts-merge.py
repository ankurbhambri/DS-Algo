# https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict

class Union:
    def __init__(self, n: int):
        self.p = list(range(n))
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

def accountsMerge(accounts):

    n = len(accounts)
    uf = Union(n)

    hm = {}
    for i in range(n):
        for email in accounts[i][1:]:
            if email in hm:
                uf.union(i, hm[email])
            hm[email] = i

    ans = defaultdict(list)
    for email, owner in hm.items():
        ans[uf.find(owner)].append(email)
    

    return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(accountsMerge(accounts))
