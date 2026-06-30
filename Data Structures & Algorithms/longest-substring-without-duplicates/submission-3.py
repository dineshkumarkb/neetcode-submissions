class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sub_string = set()

        l, r = 0, 0

        res = 0

        while r < len(s):
            while s[r] in sub_string:
                sub_string.remove(s[l])
                l += 1
            
            res = max(res, r - l + 1)

            sub_string.add(s[r])

            r += 1

        return res
        