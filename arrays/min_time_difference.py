class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_floats = [int(time[:2])*60 + int(time[3:]) for time in timePoints]
        time_floats.sort()

        min_difference = min(abs(time_floats[-1]-time_floats[0]), abs((24*60)-(time_floats[-1]-time_floats[0])))
        if min_difference == 0 or len(timePoints) == 2:
            return min_difference

        for i in range(1, len(time_floats)):
            if time_floats[i] == time_floats[i-1]:
                return 0 
            
            clockwise_difference = abs(time_floats[i]-time_floats[i-1])
            anti_clockwise_difference = abs((24*60)-(time_floats[i]-time_floats[i-1]))

            min_difference = min(min_difference, clockwise_difference, anti_clockwise_difference)
        return min_difference 
