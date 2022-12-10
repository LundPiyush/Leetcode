class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for sentence in sentences:
            count = 0
            for i in range(len(sentence)):
                if sentence[i]==' ':
                    count=count+1
            maxi = max(maxi,count)
        return maxi+1