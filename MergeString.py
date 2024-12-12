class Solution:
    def __init__(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        self.word1 = str(word1)
        self.word2 = str(word2)


    def mergeAlternately(self):
        mergeString = ""
        panjangkata = len(self.word1+self.word2)
        a = 0
        while a <= panjangkata:
            mergeString += self.word1[a]
            mergeString += self.word2[a]
            a+=1
            if a == len(self.word1):
                while a < len(self.word2):
                    a += 1  
                    mergeString += self.word2[a-1]
                break
            elif a == len(self.word2):
                while a < len(self.word1):
                    a += 1  
                    mergeString += self.word1[a-1]
                break
        return mergeString

coba = Solution("aceg","bdfh")

print(coba.mergeAlternately())
        
