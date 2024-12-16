class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n=len(nums)
        for _ in range(k):
            temp=nums[0]
            ind=0
            nums[0]=nums[0]*multiplier
            for i in range(1,n):
                if nums[i]<temp:
                    nums[ind]//=multiplier
                    ind=i
                    temp=nums[i]
                    nums[i]=nums[i]*multiplier
        return nums