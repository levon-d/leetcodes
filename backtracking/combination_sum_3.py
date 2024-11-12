class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        final = [] 

        def backtrack(curr_n, curr_k, curr_arr):
            if curr_n == 0 and curr_k == 0: 
                return curr_arr 
            if curr_arr: 
                largest = curr_arr[-1]
            else:
                largest = 0
            for i in range(largest+1, 10): 
                if (curr_n-i) >= 0 and curr_k > 0: 
                    new_k, new_n, new_arr = curr_k-1, curr_n-i, (curr_arr + [i])

                    result = backtrack(new_n, new_k, new_arr)
                    if result: 
                        final.append(result)
            
            return None 
        
        backtrack(n, k, [])
        return final

