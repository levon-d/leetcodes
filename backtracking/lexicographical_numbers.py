class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        current = 1 
        stack = [] 
        result = [] 
        
        while len(result) < n: 
            result.append(current)
            
            if current*10 > n:
                while current % 10 == 9 or current == n:
                    current = current // 10 

                current+=1                     
            else:
                current *= 10
        
        return result
