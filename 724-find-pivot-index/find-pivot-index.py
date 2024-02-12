class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        k=0
        x=[]
        for i in nums:
            k+=i
            x.append(k)
        p=0
        if x[-1]==nums[0]:
            return 0
        for i in range(1,len(nums)):
            y=x[-1]-x[i]
            if x[i-1]==y:
                return i
        return -1