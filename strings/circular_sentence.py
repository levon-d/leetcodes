class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        if len(words) <= 1:
            return sentence[0] == sentence[-1]
        
        current_last = None 

        for word in words: 
            if current_last and current_last != word[0]:
                return False 
            
            current_last = word[-1]
        
        return words[-1][-1] == words[0][0]
