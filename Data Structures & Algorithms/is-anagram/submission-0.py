class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for c in s:
            s_dict[c] = 1 + s_dict.get(c, 0)

        for c in t:
            t_dict[c] = 1 + t_dict.get(c, 0)

        for key, val in s_dict.items():
            if key not in t_dict.keys():
                return False
            if s_dict[key] != t_dict[key]:
                return False

        return True
