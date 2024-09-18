from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        counts1 = Counter(word1).values()
        counts2 = list(Counter(word2).values())

        for count in counts1:
            if count not in counts2:
                return False

            counts2.remove(count)

        return not counts2

