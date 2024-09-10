class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] < target:
            return 0 
        elif nums[0] >= target:
            return 1 
        
        minimum = float("inf")
        l = 0
        substring_total = 0
        
        for r in range(len(nums)): 
            substring_total += nums[r]

            while substring_total >= target: 
                minimum = min(r-l+1, minimum)
                substring_total -= nums[l]
                l+=1 

        return minimum if minimum != float("inf") else 0

        
