class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)
        l = 0 
        number = 1
        for r in range(len(nums)):
            if nums[r] != maximum:
                l = r 
                continue
        
            while nums[l] != maximum:
                l+=1
            
            number = max(number, r-l+1)
        
        return number 
