# https://leetcode.com/problems/smallest-sufficient-team


# TC: O(n * 2^m * 2^m) => O(n * 4^m) (n = number of people, m = number of skills)
# SC: O(2^m) (dp dictionary ke liye)
class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:

        # Har skill ko ek number id de do (0, 1, 2...)
        skill_to_id = {skill: i for i, skill in enumerate(req_skills)}
        m = len(req_skills)

        # dp dictionary: { skill_mask: [people_indexes] }
        dp = {0: []}

        # Har ek insaan ko check karo
        for i, person_skills in enumerate(people):

            # Is insaan ka skill mask banao
            person_mask = 0
            for skill in person_skills:
                if skill in skill_to_id:
                    person_mask |= (1 << skill_to_id[skill])

            # Agar iske paas koi kaam ki skill hi nahi hai, toh chhor do
            if person_mask == 0:
                continue

            # Purane saare bane hue combinations ke saath isko combine karo
            # list(dp.items()) isliye kiya taaki loop chalte waat dictionary change hone ka error na aaye
            for mask, team in list(dp.items()):

                new_mask = mask | person_mask

                # Agar yeh naya combination pehle nahi bana,
                # YA fir is naye bande ko lekar team chhoti ban rahi hai:
                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i] # Purani team + yeh naya banda

        # target_mask ka matlab saare bits 1 (jaise 3 skills ke liye 111 yani decimal 7)
        target_mask = (1 << m) - 1
        return dp[target_mask]


print(Solution().smallestSufficientTeam(["java","nodejs","reactjs"], [["java"], ["nodejs"], ["reactjs"], ["nodejs","reactjs"]])) # [0, 3]
print(Solution().smallestSufficientTeam(["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws"]])) # [1,2]