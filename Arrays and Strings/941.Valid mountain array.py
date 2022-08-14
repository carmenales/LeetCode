class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: 
            return False
        index = arr.index(max(arr))
        if index == 0 or index == len(arr) -1: 
            return False
        for i in range(1, len(arr)):
            if i <= index:
                if arr[i] <= arr[i - 1]: 
                    return False
            else:
                if arr[i] >= arr[i - 1]: 
                    return False
        return True
