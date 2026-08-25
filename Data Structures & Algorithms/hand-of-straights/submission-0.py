class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False

        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:

            min_val = min_heap[0]

            # iterate from min to group size
            for i in range(min_val, min_val + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True


        
        