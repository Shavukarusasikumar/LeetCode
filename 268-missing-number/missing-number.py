class Solution:
    def missingNumber(self, n: List[int]) -> int:
        n1=[i for i in range(0,len(n))]
        n.sort()
        for i in range(0,len(n1)):
            if(n[i]!=n1[i]):
                return n1[i]
        return n[-1]+1