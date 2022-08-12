class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        index = 0
        p = {"(": ")", "[": "]", "{": "}"}
        finish = 0
        if len(s) < 2:
            return 0
        while(finish == 0):
            if s == "":
                return 1
            elif len(s) == 1:
                return 0
            elif (s[index] in p):
                if (index < len(s)-1) and (s[index+1] == p[s[index]]):
                    s = s.replace(s[index]+s[index+1], "")
                    if index > 0:
                        index -= 1
                elif (index < len(s)-1) and s[index+1] in p:
                    index += 1 
                else:
                    finish = 1
            elif index == 0:
                return 0
            else:
                index += 1 

        return 0
