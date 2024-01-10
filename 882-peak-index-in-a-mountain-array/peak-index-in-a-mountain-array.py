class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        k=arr[0]
        ind=0
        for i in range(1,len(arr)):
            if arr[i]>k:
                k=arr[i]
                ind=i
        return ind