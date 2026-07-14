class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # char count of t
        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)


        res_len = float("inf")
        res = [-1, -1]


        curr_window = {}

        have, need = 0, len(t_count)

        
        # init sliding window
        l = 0
        for r in range(len(s)):
            char = s[r]
            curr_window[char] = 1 + curr_window.get(char, 0)
        
            if char in t_count and curr_window[char] == t_count[char]:
                have += 1
                
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                curr_window[s[l]] -= 1
                if s[l] in t_count and curr_window[s[l]] < t_count[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res

        return s[l: r + 1] if res_len != float("inf") else ""




        