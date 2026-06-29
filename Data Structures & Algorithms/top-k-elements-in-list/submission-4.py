class Solution:
    def topKFrequent(self, nums: List[int], target: int) -> List[int]:

        # get a count map
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)


        arr = []

        for num, freq in count.items():
            heapq.heappush(arr,[freq, num])

            if len(arr) > target:
                heapq.heappop(arr)

        res = []

        for i in range(target):
            res.append(heapq.heappop(arr)[1])

        return res
