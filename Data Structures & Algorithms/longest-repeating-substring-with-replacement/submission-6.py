class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

       

        res = 0

        max_f = 0

        l = 0

        char_count = {}

        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            max_f = max(max_f, char_count[s[r]])

            while (r - l + 1) - max_f > k:
                char_count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res




        


        