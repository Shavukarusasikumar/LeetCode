class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        strs.sort()
        s1=strs[0]
        s2=strs[-1]
        n=len(s2)
        s=''
        for i in range(len(s1)):
            if i<n and s1[i]==s2[i]:
                s+=s1[i]
            else:
                return s
        return s
