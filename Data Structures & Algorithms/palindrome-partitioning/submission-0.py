class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def is_pal(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        
        def dfs(i, curr):

            if i >= len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                if is_pal(i, j, s):
                    curr.append(s[i: j + 1])
                    dfs(j + 1, curr)
                    curr.pop() 

        
        dfs(0, [])

        return res
        