class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        end_count = {}
        for i, c in enumerate(s):
            end_count[c] = i

        size=end=0

        res = []

        for i,c in enumerate(s):

            size += 1
            end = max(end, end_count[c])

            if i == end:
                res.append(size)
                size = 0

        return res

        