class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        import numpy as np
        nums = sorted(np.abs(nums))
        return [x*x for x in nums]
