class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)/2
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>n:
                n=d[i]
                ans=i
        return ans
        
        