class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k = k%total
        current = 0 

        while k >= chalk[current]:
            k-=chalk[current] 
            current = (current+1)%len(chalk)
        
        return current
