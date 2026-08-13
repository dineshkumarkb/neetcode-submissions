class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # koko can eat bananas from minimum 1 to max(piles) i.e the value of k
        # use binary search to find the value of k
        # rate = p[i] / k (ceil value)

        l = 1
        r = max(piles)

        res = float("inf")

        while l <= r:

            k = (l + r) // 2

            hours = 0

            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1

        return res




        