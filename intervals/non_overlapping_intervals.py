class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        if len(intervals) == 1:
            return 0 

        previous = 0
        result = 0
        for i in range(1, len(intervals)):

            previous_start, previous_end = intervals[previous][0], intervals[previous][1]
            current_start, current_end = intervals[i][0], intervals[i][1]

            if previous_end <= current_start:
                previous = i 
                continue
            
            if current_end < previous_end:
                previous = i

            result += 1 
        
        return result 
