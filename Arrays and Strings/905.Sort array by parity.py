class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_list = []
        odd_list = []
        for i in range(len(nums)):
            if (nums[i]%2) == 0:
                # Even
                even_list.append(nums[i])
            else:
                # Odd
                odd_list.append(nums[i])
                
        nums = even_list + odd_list
        return nums
