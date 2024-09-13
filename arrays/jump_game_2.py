class Solution:
    def jump(self, nums: List[int]) -> int:
        prefix = [0]

        for i in range(len(nums)-2, -1, -1): 
            jump = nums[i]
            if i + jump >= len(nums)-1:
                prefix = [1] + prefix
                continue  
            # steps = 1 + prefix[jump-1]
            minimum_steps = float("inf")
            for j in range(jump): 
                minimum_steps = min(prefix[j], minimum_steps)
            
            minimum_steps += 1 

            prefix = [minimum_steps] + prefix 
        
        return prefix[0]
