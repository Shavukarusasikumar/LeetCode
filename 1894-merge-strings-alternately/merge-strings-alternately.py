class Solution:
    def mergeAlternately(self, n1: str, n2: str) -> str:
        s=''
        if len(n1)>len(n2):
            n=len(n1)
        else:
            n=len(n2)
        k1=len(n1)-1
        k2=len(n2)-1
        for i in range(n):
            if i<=k1:
                s+=n1[i]
            if i<=k2:
                s+=n2[i]
        return s