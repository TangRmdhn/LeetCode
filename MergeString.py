class Solution:

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
        
