class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        end = 0 
        max_len = 0

        for end in range(len(s)):
            if s[end] in s[start : end]:
                while s[start] != s[end]:
                    start +=1
                start +=1
            
            else:
                max_len = max(max_len, end-start+1)
            
        return max_len
