class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_array = len(set(nums))
        sorted_array = sorted(set(nums))
        if unique_array == 2:
            return sorted_array[-1]
        elif unique_array == 1:
            return nums[0]
        else:
            return sorted_array[-3]
