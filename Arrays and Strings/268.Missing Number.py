class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for index, i in enumerate(nums):
            if index != i:
                return index
        return index+1
