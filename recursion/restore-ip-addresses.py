class Solution:
    def restoreIpAddresses(self, s):

        res = []

        def helper(s_tmp, idx, path):

            if idx > 4:
                return 

            if idx == 4 and not s_tmp:
                res.append(path[:-1])
                return

            for i in range(1, len(s_tmp) + 1):
 
                if s_tmp[:i] == '0' or (s_tmp[0] != '0' and 0 < int(s_tmp[:i]) < 256):

                    helper(s_tmp[i:], idx + 1, path + s_tmp[:i] + ".")


        helper(s, 0, "")

        return res

print(Solution().restoreIpAddresses("0000"))  # ["0.0.0.0"]
print(Solution().restoreIpAddresses("25525511135"))  # ["255.255.11.135", "255.255.111.35"]
