class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        
        dp = [0] * (len(s)+1)

        for i in range(len(s)-1, -1, -1):
            dp[i] = dp[i+1] + 1 

            for length in range(1, len(s)-i+1):
                if s[i:i+length] in dictionary:
                    dp[i] = min(dp[i], dp[i+length])
        
        return dp[0]
