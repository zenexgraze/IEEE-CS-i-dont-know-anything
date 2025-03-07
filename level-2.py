from bisect import bisect_left, insort

class IntervalMerger:
    def __init__(self):
        self.intervals = []  # Sorted list of merged intervals

    def addInterval(self, start, end):
        # Find the correct insertion point using binary search
        i = bisect_left(self.intervals, (start, end))

        # Merge with left overlapping intervals
        while i > 0 and self.intervals[i - 1][1] >= start:
            i -= 1

        # Merge with right overlapping intervals
        while i < len(self.intervals) and self.intervals[i][0] <= end:
            start = min(start, self.intervals[i][0])
            end = max(end, self.intervals[i][1])
            self.intervals.pop(i)  # Remove merged interval

        # Insert the new merged interval in the correct position
        # insort(self.intervals, (start, end))
        self.intervals.insert(i, (start, end))

    def getIntervals(self):
        return self.intervals

merger = IntervalMerger()
merger.addInterval(1, 5)
merger.addInterval(6, 8)
merger.addInterval(9, 11)
merger.addInterval(7, 10)
print(merger.getIntervals()) 
