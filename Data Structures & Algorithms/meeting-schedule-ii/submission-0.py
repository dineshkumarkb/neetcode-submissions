"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])

        s, e = 0, 0

        rooms, count = 0, 0

        while s < len(start_times):
            if start_times[s] < end_times[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            rooms = max(rooms, count)

        return rooms


        