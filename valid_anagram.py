class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

    
        unique_s = list(set(s))
        unique_t = list(set(t))

        dict_s = {}
        dict_t = {}
        for i in unique_s:
            count_s = s.count(i)
            dict_s[i] = count_s
        
        for i in unique_t:
            count_t = t.count(i)
            dict_t[i] = count_t

        if Counter(dict_s) == Counter(dict_t):
            return True
        else:
            return False
