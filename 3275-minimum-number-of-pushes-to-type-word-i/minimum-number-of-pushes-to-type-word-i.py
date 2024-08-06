class Solution:
    def minimumPushes(self, word: str) -> int:
        c = 0
        bc = 0
        for i in range (len(word)):
            c += 1
            if c < 9:
                bc += 1
            elif c < 17:
                bc += 2
            elif c<25:
                bc += 3
            else:
                bc+=4
        return bc