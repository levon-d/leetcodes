class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final = nums[0] 
        current = 0 

        for num in nums: 
            if current < 0: 
                current = 0 

            current += num 
            final = max(final, current)
        
        return final
