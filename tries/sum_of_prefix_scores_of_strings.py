class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = [None] * 26
    

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root 
        for char in word:
            i = ord(char) - ord("a")
            if not current.children[i]:
                current.children[i] =  TrieNode()
            current = current.children[i]
            current.count += 1 
    
    def get_score(self, word):
        current = self.root
        score = 0

        for char in word: 
            i = ord(char) - ord("a")
            current = current.children[i]
            score += current.count
        
        return score

    

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []    
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        for word in words:
            res.append(trie.get_score(word))

        return res 
