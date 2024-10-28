class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_sorted = sorted(nums)

        curr_index = 0 
        longest = 1
        curr_num = nums_sorted[0]
        curr_subsequence_length = 1
        while curr_index < len(nums): 
            while (curr_num ** 2) in nums_set:
                curr_num = curr_num ** 2 
                curr_subsequence_length += 1 

            longest = max(longest, curr_subsequence_length)

            curr_index += 1 
            if curr_index < len(nums):
                curr_num = nums[curr_index]
                curr_subsequence_length = 1

        return longest if longest > 1 else -1



        
        
