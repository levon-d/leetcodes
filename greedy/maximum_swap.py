class Solution:
    def maximumSwap(self, num: int) -> int:
        result = num

        arr = []
        while num:
            arr = [(num % 10)] + arr
            num = num // 10

        highest = []
        max_so_far = (arr[-1], len(arr) - 1)
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > max_so_far[0]:
                max_so_far = (arr[i], i)
            highest = [max_so_far] + highest

        for i in range(len(arr)):
            if arr[i] < highest[i][0]:
                arr[i], arr[highest[i][1]] = arr[highest[i][1]], arr[i]
                break

        result = int("".join(map(str, arr)))
        return result
