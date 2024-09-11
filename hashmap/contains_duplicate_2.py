class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_index_mapping = {} 

        for i in range(len(nums)): 
            if nums[i] in value_index_mapping:
                j = value_index_mapping[nums[i]]
                if abs(i-j) <= k:
                    return True 
            value_index_mapping[nums[i]] = i 
    
        return False 
