class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        count = 0
        for i in range(n-1):
            if timeSeries[i] + duration - 1 < timeSeries[i+1]:
                count+=duration
            else:
                count = count + timeSeries[i+1] - timeSeries[i]
        return count + duration