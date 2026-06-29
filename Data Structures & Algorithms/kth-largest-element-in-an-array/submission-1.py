class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using max_heap
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        print(max_heap)

        for i in range(k):
            val = heapq.heappop(max_heap)

        return -val

        