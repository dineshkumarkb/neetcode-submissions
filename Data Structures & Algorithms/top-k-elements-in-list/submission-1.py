class Solution:
    def topKFrequent(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}

        arr = []

        for n in nums:
            my_dict[n] = 1 + my_dict.get(n, 0)

        for k, v in my_dict.items():
            arr.append([v, k])

        arr.sort()

        res = []

        while len(res) < target:
            res.append(arr.pop()[1])

        return res
        