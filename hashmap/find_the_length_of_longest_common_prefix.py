class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        result = 0
        arr1_prefix_set = set()
        for num in arr1:
            while num: 
                arr1_prefix_set.add(num)
                num = num // 10 
        
        for num in arr2: 
            while num: 
                if num in arr1_prefix_set:
                    result = max(len(str(num)), result)
                    break 
                num = num // 10 
        
        return result 
