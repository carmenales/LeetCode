class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, 
                   "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
        
        sum = 0
        i = 0
        l = len(s)
        while (i < l):
            if s[i:i+2] in symbols:
                sum += symbols[s[i:i+2]]
                i += 2
            else:
                sum += symbols[s[i]]
                i += 1
                
        return sum
