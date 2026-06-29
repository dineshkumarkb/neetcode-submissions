class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # choose the heaviest stones.max heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            
            s1 = -1 * heapq.heappop(max_heap)
            s2 = -1 * heapq.heappop(max_heap)

            if s1 != s2:
                if s1 < s2:
                    heapq.heappush(max_heap, (s1 - s2))
                else:
                    heapq.heappush(max_heap, (s2 - s1))

        return (-1 * max_heap[0]) if max_heap else 0



        