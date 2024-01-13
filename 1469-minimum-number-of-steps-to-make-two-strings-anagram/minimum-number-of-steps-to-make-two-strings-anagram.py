class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1={}
        d2={}
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]]+=1
            else:
                d1[s[i]]=1
            if t[i] in d2:
                d2[t[i]]+=1
            else:
                d2[t[i]]=1
        c=0
        for i,j in d2.items():
            if i in d1:
                d1[i]-=j
        for i in d1.values():
            if i>0:
                c+=i
        return c