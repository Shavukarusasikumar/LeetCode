class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        k=max(d.values())
        c=0
        for i in d.values():
            if i==k:
                c+=1
        return c*k