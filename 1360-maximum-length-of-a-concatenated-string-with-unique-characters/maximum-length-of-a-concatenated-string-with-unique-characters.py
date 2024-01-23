class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def fun(s):
            return len(s)==len(set(s))
        n = len(arr)
        p = 1 << n
        m = 0
        for i in range(p):
            s=""
            for j in range(n):
                if i&(1<<j):
                    s+=arr[j]
            if fun(s):
                m=max(m,len(s))
        return m
            
            