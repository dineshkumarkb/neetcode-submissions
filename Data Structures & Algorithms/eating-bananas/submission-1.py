class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            t = 0

            for p in piles:
                t += math.ceil(p /k)
            
            if t <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1

        return res

            


        