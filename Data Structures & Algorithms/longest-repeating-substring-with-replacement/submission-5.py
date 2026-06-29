class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window_count = {}

        l = 0

        res = 0

        for r in range(len(s)):
            window_count[s[r]] = 1 + window_count.get(s[r], 0)

            if (r - l + 1) - max(window_count.values()) > k:
                window_count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

        