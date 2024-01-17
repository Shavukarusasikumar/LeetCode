class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in d.values():
            if i in l:
                return False
            l.append(i)
        return True
