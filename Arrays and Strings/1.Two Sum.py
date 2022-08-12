class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for indx, i in enumerate(nums):
            for jndx, j in enumerate(nums[indx+1:]):
                sum = i+j
                if target == sum:
                    return [indx,jndx+indx+1]

