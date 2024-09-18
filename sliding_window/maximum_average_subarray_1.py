class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        

        current_sum = sum(nums[:k])
        max_sum = current_sum
        l = 0
        
        for r in range(k, len(nums)): 
            current_sum = current_sum - nums[l] + nums[r]
            max_sum = max(current_sum, max_sum)
            l+=1

        return (max_sum / k)
