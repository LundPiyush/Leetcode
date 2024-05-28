class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return -1

        for i in range(len(haystack) + 1 - len(needle)):
            # running the outer loop from 0 till len(s1)-len(s2)
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
