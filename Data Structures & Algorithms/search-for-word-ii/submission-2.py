class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res = set()

        class TrieNode:

            def __init__(self):
                self.children = {}
                self.end_word = False

            def add_word(self, word: str):
                curr = self
                for c in word:
                    if c not in curr.children:
                        curr.children[c] = TrieNode()
                    curr = curr.children[c]
                curr.end_word = True

        
        root = TrieNode()
        for w in words:
            root.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, node, curr):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r, c))

            node = node.children[board[r][c]]
            curr += board[r][c]

            if node.end_word:
                res.add(curr)

            dfs(r + 1, c, node, curr)
            dfs(r, c + 1, node, curr)
            dfs(r - 1, c, node, curr)
            dfs(r, c - 1, node, curr)

            visit.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)


        