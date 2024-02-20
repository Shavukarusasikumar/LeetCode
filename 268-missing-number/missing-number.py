class Solution:
    def missingNumber(self, n: List[int]) -> int:
        n.sort()
        for i in range(0,len(n)):
            if(n[i]!=i):
                return i
        return i+1