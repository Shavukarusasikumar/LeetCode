class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=0
        l=[]
        for i in nums:
            ans+=i
            l.append(ans)
        return l