"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()
        start_idx = 0
        end_idx = 0

        count = 0
        max_count = 0

        while start_idx < len(starts):
            if starts[start_idx] < ends[end_idx]:
                count += 1
                start_idx += 1
            else:
                count -= 1
                end_idx += 1

            max_count = max(max_count, count)

        return max_count
