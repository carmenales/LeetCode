class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr=[]
        for i in range(len(arr)-1):
            arr_r = max(arr[i+1:])
            new_arr.append(arr_r)
        new_arr.append(-1)
        return new_arr
