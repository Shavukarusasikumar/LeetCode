class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        c=nums.count(1)
        nums=nums+nums[:c] 
        k=sum(nums[:c])
        min_val=c-k
        for i in range(c,len(nums)):
            k+=nums[i]-nums[i-c]
            min_val=min(min_val,c-k)
        return min_val
       
        