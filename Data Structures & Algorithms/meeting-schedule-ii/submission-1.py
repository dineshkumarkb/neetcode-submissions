"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # 2 separate arrays for start and end
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = 0
        count = 0

        # 2 pointers
        s, e = 0, 0

        while s < len(intervals):

            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1

            res = max(count, res)


        return res
        