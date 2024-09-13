import math
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        if len(nums) < 2:
            return 0 

        gcds = {}

        pairs = 0 

        for num in nums:
            gcd = math.gcd(num, k)

            for key in gcds.keys():
                if gcd * key % k == 0:
                    pairs += gcds[key]
            
            gcds[gcd] = gcds.get(gcd, 0) + 1 
        return pairs
