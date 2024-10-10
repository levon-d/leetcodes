class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0] * len(nums)
        i = len(nums)-1
        prev_max = 0
        for num in reversed(nums):
            max_right[i] = max(num, prev_max)
            prev_max = max_right[i]
            i -= 1 

        result = 0 
        l = 0 

        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l+=1

            result = max(result, r-l)
        
        return result
