class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        if not nums:
            return None
        
        length = len(nums)
        for i in range(length):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        for i in range(length):
            if nums[i] > 0:
                result.append(i + 1)
        return result
