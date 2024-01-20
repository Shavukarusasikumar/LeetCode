class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        n=len(strs)
        m={}
        for i in range(n):
            k="".join(sorted(strs[i]))
            if k in m:
                m[k].append(i)
            else:
                m[k]=[i]
        ans=[]
        for i,j in m.items():
            temp=[]
            for k in j:
                temp.append(strs[k])
            ans.append(temp)
        return ans

