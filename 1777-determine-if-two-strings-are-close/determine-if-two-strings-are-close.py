class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        x = Counter(w1)
        y = Counter(w2)
        a = Counter(x.values())
        b = Counter(y.values())
        c = a - b
        return x.keys() == y.keys() and len(c) == 0