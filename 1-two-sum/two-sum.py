class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        l=len(nums)
        c=[]
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==t:
                    return [i,j]