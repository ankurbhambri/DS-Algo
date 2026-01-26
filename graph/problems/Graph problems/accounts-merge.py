# https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict

# TC: O(N K log (N K)) where N is number of accounts, K is max number of emails in an account
# SC: O(N K) for union find and hashmap
class Union:
    def __init__(self, n: int):
        self.p = list(range(n))
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts):

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
print(Solution().accountsMerge(accounts))


# Variant

'''
Given a list of accounts where each element is an entry in a map, where the key is an ID, and the value is a list of emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same group of IDs of the same person if there is some common email to both accounts.
A person can have any number of IDs. After merging the accounts, return the accounts in the following format: the elements of each account are all of the IDs of the same person.
The accounts themselves can be returned in any order.

Example 1:

Input:
    accounts = [{"C1": ["a", "b"]}, {"C2": ["c"]}, {"C3": ["b", "d"]}, {"C4": ["d"]}, {"C5": ["e"]}, {"C6": ["c"]}, {"C7": ["a"]}]

Output: [[C1, C3, C4, C7], [C2, C6], [C5]]

Explanation:
    C1, C3, C4 and C7 are IDs of the same person as they have the common email "a" and "b".
    C5 is an ID of a different person as none of their email addresses are used by other accounts.
    We could return these lists in any order, for example the answer [ [C2, C6], [C1, C3, C4, C7], [C5]] would still be accepted.

'''

def mergeAccounts(accounts):

    n = len(accounts)
    uf = Union(n)

    hm = {}
    for i in range(n):
        for _, emails in accounts[i].items():
            for email in emails:
                if email in hm:
                    uf.union(i, hm[email])
                hm[email] = i

    ans = defaultdict(set)
    for i in range(n):
        root = uf.find(i)
        current_id = list(accounts[i].keys())[0]
        ans[root].add(current_id)

    return [sorted(list(group)) for group in ans.values()]


print(mergeAccounts([{"C1": ["a", "b"]}, {"C2": ["c"]}, {"C3": ["b", "d"]}, {"C4": ["d"]}, {"C5": ["e"]}, {"C6": ["c"]}, {"C7": ["a"]}])) # Output: [[C1, C3, C4, C7], [C2, C6], [C5]]