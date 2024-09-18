class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        l = 0
        k_used_in_current_window = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k_used_in_current_window += 1

            while k_used_in_current_window > k:
                if nums[l] == 0:
                    k_used_in_current_window -= 1
                l += 1

            result = max(result, r - l + 1)
        return result
