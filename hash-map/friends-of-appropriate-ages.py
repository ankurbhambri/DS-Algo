# https://leetcode.com/problems/friends-of-appropriate-ages/submissions/1897061428/

# TC: O(n + m) where n is number of ages and m is the range of ages (1 to 120)
# SC: O(1)
class Solution:
    def numFriendRequests(self, ages):

        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        ans = 0
        for ageA in range(1, 121):
            for ageB in range(1, 121):
                # Conditions check karein (Negative logic ka reverse)
                if not (ageB <= 0.5 * ageA + 7 or ageB > ageA or (ageB > 100 and ageA < 100)):
                    if ageA == ageB:
                        ans += count[ageA] * (count[ageA] - 1)
                    else:
                        ans += count[ageA] * count[ageB]
        return ans


# Sorting + Binary Search approach

# TC: O(n log n)
# SC: O(1)
class Solution:
    def numFriendRequests(self, ages):

        ans = 0
        ages.sort()
        n = len(ages)

        for i in range(n):

            ageA = ages[i]

            if ageA <= 14:
                continue # Rule 1: 14 se chhote log kisi ko nahi bhej sakte

            # 1. Sabse pehla banda dhundo jo request receive kar sake
            # Condition: ageB > 0.5 * ageA + 7
            limit = 0.5 * ageA + 7
            L = bisect.bisect_right(ages, limit)

            # 2. Sabse aakhri banda dhundo jiski age <= ageA
            # bisect_right hume current age ke khatam hone ka index dega
            R = bisect.bisect_right(ages, ageA) - 1

            # 3. Agar range valid hai, toh count add karein
            if R >= L:
                ans += (R - L) # (R - L + 1) log hain, minus 1 (khud ke liye)

        return ans


# Variant:

'''

A group of centaurs (mythical half-human, half-horse creatures) all sign up for Facebook accounts at the same time.

They immediately start sending each other friend requests, in accordance with the ancient rules that have governed centaur friendship since the dawn of time:

1. A centaur will only send a friend request to another centaur if the recipient is at least (X/2 + 7) of the sender's age. For example,
        a 200-year old centaur can only send friend requests to centaurs that are at least 107 years old.
2. A centaur will not send a friend request to another centaur that is older than it is.
3. A centaur over 100 years old will not send a friend request to a recipient under 100 years old. But centaurs under 100 years old can friend each other.
4. If any of the conditions for sending a friend request are not met, no friend request will be sent.

Write a function that, given an array of centaur ages, returns an integer of the total number of friend requests that the group of centaurs will send to each other.

    c = [120, 110] # 1
    c = [120,110,99] # 1
    c = [100,110,120] # 3
    c = [120,45,230,400,88,300,101] # 4
    c = [101, 120, 230, 400, 88, 45, 55, 300] # 6

'''

import bisect


# Sorting + Binary Search approach

# TC: O(n log n)
# SC: O(1)
def numFriendRequests(ages):

    ages.sort()
    ans = 0
    n = len(ages)

    for i in range(n):
        ageA = ages[i]
        if ageA <= 14: continue
        
        # 1. Lower Bound: Sabse pehla index 'L' jahan age > (0.5 * ageA + 7)
        limit = 0.5 * ageA + 7

        # bisect_right hume wo index deta hai jahan 'limit' se badi value shuru ho rahi hai
        L = bisect.bisect_right(ages, limit)
        
        # 2. Upper Bound: Sabse aakhri index 'R' jahan age == ageA
        # Kyunki array sorted hai, toh ageA wale log line se honge
        R = bisect.bisect_right(ages, ageA) - 1
        
        # 3. Rule 3 (Centaur Special): 100+ wala 100- ko nahi bhej sakta
        # Agar AgeA > 100 hai, toh humara L kam se kam 100 wale index par hona chahiye
        if ageA > 100:
            index_100 = bisect.bisect_left(ages, 100)
            L = max(L, index_100)

        # Agar valid range hai, toh total bande = (R - L + 1)
        # Par banda khud ko request nahi bhej sakta, toh -1
        if R >= L:
            ans += (R - L)
            
    return ans

print(numFriendRequests([120, 110])) # 1
print(numFriendRequests([120,110,99])) # 1
print(numFriendRequests([100,110,120])) # 3
print(numFriendRequests([120,45,230,400,88,300,101])) # 4
print(numFriendRequests([101, 120, 230, 400, 88, 45, 55, 300])) # 6