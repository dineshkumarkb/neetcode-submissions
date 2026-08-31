class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        res = 0

        # sort the intervals
        intervals.sort(key=lambda x: x[1])

        # keep track of prev interval
        prev_end = intervals[0][-1]

        for i in range(1, len(intervals)):

            if intervals[i][0] < prev_end:
                res += 1
            else:
                prev_end = intervals[i][1]

        return res
        