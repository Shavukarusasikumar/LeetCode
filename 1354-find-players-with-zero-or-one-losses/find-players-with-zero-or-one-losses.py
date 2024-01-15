class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        l=set()
        for i in range(len(matches)):
            l.add(matches[i][0])
            l.add(matches[i][1])
            if matches[i][1] in d:
                d[matches[i][1]]+=1
            else:
                d[matches[i][1]]=1
        l1,l2=[],[]
        l=list(l)
        l.sort()
        for i in l:
            k=d.get(i,0)
            if k==0:
                l1.append(i)
            elif k==1:
                l2.append(i)
        x=[l1,l2]
        return x