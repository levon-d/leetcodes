from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()

        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for word in s1:
            s1_map[word] += 1 
        for word in s2: 
            s2_map[word] += 1 
        
        s1_single_words = [word for word in s1_map.keys() if s1_map[word] == 1]
        s2_single_words = [word for word in s2_map.keys() if s2_map[word] == 1]

        result = []

        for word in s1_single_words:
            if word not in s2_map:
                result.append(word)

        for word in s2_single_words:
            if word not in s1_map:
                result.append(word)
        
        return result
