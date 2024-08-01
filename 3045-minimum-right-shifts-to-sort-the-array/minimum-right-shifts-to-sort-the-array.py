class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        k=sorted(nums)
        c=0
        n=len(nums)
        while True:
            if nums==k:
                return c
            temp=nums.pop()
            nums.insert(0,temp)
            c+=1
            if c==n:
                return -1
            