class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d={5:0,10:0}
        for i in bills:
            if i==5:
                d[5]+=1
            elif i==10:
                if d[5]!=0:
                    d[5]-=1
                    d[10]+=1
                else:
                    return False
            else:
                if d[10]!=0 and d[5]!=0:
                    d[10]-=1
                    d[5]-=1
                elif d[5]>2:
                    d[5]-=3
                else:
                    return False
        return True