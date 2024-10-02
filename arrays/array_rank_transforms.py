class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {} 
        sorted_arr = sorted(list(set(arr)))
        for i, num in enumerate(sorted_arr):
            ranks[num] = i+1 
        
        for i, num in enumerate(arr): 
            arr[i] = ranks[num]
        
        return arr
