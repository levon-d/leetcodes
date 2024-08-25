"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        index_per_diff = {}
        index_per_diff[0] = -1
        max_length, count = 0, 0
        
        for i in range(len(nums)):
            increment = 1 if nums[i] == 1 else -1 
            count += increment 
            if count in index_per_diff:
                max_length = max(max_length, i - index_per_diff[count])
            else:
                index_per_diff[count] = i 
        
        return max_length 
