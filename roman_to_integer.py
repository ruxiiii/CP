class Solution:
    def romanToInt(self, s: str) -> int:
        t = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":            500,
            "M":             1000,
            "IV":           4,
            "IX":           9,
            "XL":           40,
            "XC":           90,
            "CD":              400,
            "CM":               900


        }

        number = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and ((s[i]=="I" and (s[i+1]=="V" or s[i+1]=="X")) or (s[i]=="X" and (s[i+1]=="L" or s[i+1]=="C")) or (s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M"))):
                z = s[i]+ s[i+1]
                number += t[z]
                i += 2
            else:
                number += t[s[i]]
                i += 1
        return number
