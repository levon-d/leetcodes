class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0 
        nums = [num for num in nums if num!=0]
        while nums:
            x = min(nums)
            nums = [(n-x) for n in nums if (n-x) > 0]
            operations+=1 

        return operations
