class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n=len(nums)
        for _ in range(k):
            temp=nums[0]
            ind=0
            
            for i in range(1,n):
                if nums[i]<temp:
                    ind=i
                    temp=nums[i]
            nums[ind]=nums[ind]*multiplier
        return nums