class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        # the maximum value of k only could be the max(piles)
        r = max(piles)

        res = float("inf")

        while l <= r:

            mid = (l + r) // 2

            hours = 0

            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1

        return res




        