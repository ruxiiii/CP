class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''first length of needle
        then the first occurance of needle in haystack
        if length needle<len hay return -1
        '''

        if not needle:
            return (-1)

      
        
        len_needle = len(needle)
        difference_length = len(haystack) - len(needle)

        for i in range(difference_length + 1):
            if haystack[i:(len(needle) + i)] == needle:
                return i
            
        return (-1)

