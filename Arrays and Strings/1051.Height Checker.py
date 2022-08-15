class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        for current_height, desired_height in zip(heights, sorted(heights)):
            if current_height != desired_height:
                count += 1
        return count
