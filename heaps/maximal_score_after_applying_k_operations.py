import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        negated = [-num for num in nums]
        heapq.heapify(negated)
        result = 0
        for i in range(k): 
            elem = -heapq.heappop(negated)
            result += elem 
            new_elem = math.ceil(elem/3)
            heapq.heappush(negated, -new_elem)
        return result
