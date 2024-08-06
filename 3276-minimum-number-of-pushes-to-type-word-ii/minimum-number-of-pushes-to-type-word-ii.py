class Solution:
    def minimumPushes(self, word: str) -> int:
        d=Counter(word)
        d=sorted(d.values(),reverse=True)
        c = 0
        bc = 0
        
        for i in d:
            c += 1
            if c < 9:
                bc += i
            elif c < 17:
                bc += (2 * i)
            elif c<25:
                bc += (3 * i)
            else:
                bc+=(4*i)
            
        # print(c,bc,len(word),len(k),k)
        return bc