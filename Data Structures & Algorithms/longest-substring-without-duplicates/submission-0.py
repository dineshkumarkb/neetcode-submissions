class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l,r = 0, 0

        temp = set()

        res = 0

        while r < len(s):

            while s[r] in temp:
                temp.remove(s[l])
                l += 1
            
            temp.add(s[r])

            res = max(res, (r - l + 1))

            r += 1

        return res


                

        