class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        for i in word:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        k = list(d.values())
        k.sort(reverse=True)
        c = 0
        bc = 0
        
        for i in k:
            c += 1
            if c < 9:
                bc += i
            elif c < 17:
                bc += (2 * i)
            elif c<25:
                bc += (3 * i)
            else:
                bc+=(4*i)
            
        print(c,bc,len(word),len(k),k)
        return bc