class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # scenarios

        res = []

        def dfs(openP, curr, closeP):

            if openP == closeP == n:
                res.append("".join(curr))
                return

            if openP < n:
                curr.append("(")
                dfs(openP + 1, curr, closeP)
                curr.pop()

            
            if closeP < openP:
                curr.append(")")
                dfs(openP, curr, closeP + 1)
                curr.pop()

        
        dfs(0, [], 0)
        return res

        