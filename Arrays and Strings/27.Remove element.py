class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        
        if length == 0:
            return length
        
        i = 0
        while i < length:
            if nums[i] == val:
                del nums[i]
                length = length-1
            else:
                i = i+1
