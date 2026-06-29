class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_map = {}

        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        need = len(t_map)

        have = 0

        window_count = {}

        l = 0

        res_len = float('inf')
        res = [-1, -1]

        for r in range(len(s)):
            c = s[r]
            window_count[c] = 1 + window_count.get(c, 0)
            if c in t_map and window_count[c] == t_map[c]:
                have += 1

            # shrink logic
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = [l, r]
                window_count[s[l]] -= 1
                if s[l] in t_map and window_count[s[l]] + 1 == t_map[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l: r + 1] if res_len != float('inf') else ""
                

        