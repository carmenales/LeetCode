class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "" and haystack == "":
            return 0

        if needle in haystack:
            return (haystack.find(needle))
        else:
            return -1
