class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re

        paragraph = paragraph.lower()
        words = re.split(r'\W+', paragraph)
        words = list(filter(None, words))

        max_count = 0
        result = ""
        for i in words:
            if i not in banned:
                count = words.count(i)
                if max_count < count:
                    max_count = count
                    result = i
        return result
