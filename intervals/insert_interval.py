class Solution:

    def binary_search(self, arr, target):
        if arr[0][0] == target:
            return 0
        if arr[-1][0] == target:
            return len(arr) - 1

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        return l

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        insertion = self.binary_search(intervals, newInterval[0])
        result = []
        new_intervals = intervals[:insertion] + [newInterval] + intervals[insertion:]

        for i in range(len(new_intervals)):
            if not result or new_intervals[i][0] > result[-1][1]:
                result.append(new_intervals[i])
                continue

            if new_intervals[i][0] <= result[-1][1]:
                previous = result.pop()
                new = [
                    min(previous[0], new_intervals[i][0]),
                    max(previous[1], new_intervals[i][1]),
                ]
                result.append(new)

        return result
