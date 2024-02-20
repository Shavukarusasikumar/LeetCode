class Solution:
    def missingNumber(self, n: List[int]) -> int:
        n1=0
        n.sort()
        for i in range(0,len(n)):
            if(n[i]!=n1):
                return n1
            n1+=1
        return n[-1]+1