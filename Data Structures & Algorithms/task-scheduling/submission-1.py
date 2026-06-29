class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_count = {}
        for t in tasks:
            task_count[t] = 1 + task_count.get(t, 0)

        max_heap = [-c for c in task_count.values()]

        q = deque()

        time = 0

        while q or max_heap:

            # calc idle time
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
                    


        