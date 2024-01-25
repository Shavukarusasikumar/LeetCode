class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        for i in arr1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in arr2:
            k=d.get(i,0)
            for j in range(k):
                l.append(i)
        x=[]
        for i in arr1:
            if i not in arr2:
                x.append(i)
        # lst=l+x
        x.sort()
        return l+x



