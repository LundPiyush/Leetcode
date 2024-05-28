class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s1 = s[::1]

        j = 0
        for i in range(len(s)-1,-1,-1):
            s[j] = s1[i]
            j = j+1

        