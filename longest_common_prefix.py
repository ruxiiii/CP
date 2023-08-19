class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==0:
            return ""
        else: 
            #we have s as the shortest length word in the array
            s = min(strs, key=len)
            i=0
            str = ""
            for i in range(len(s)):
                for j in range(len(strs)):
                    if s[i] == strs[j][i]:
                        continue
                    else:
                        return str         
                str = str + s[i]
            return str

sol = Solution()
strs = ["dog","docecar","dor"]
sol.longestCommonPrefix(strs)
