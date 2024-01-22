class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        c=len(s)
        while c:
            if s==goal:
                return True
            c-=1
            k=s[0]
            s=s[1:]+k
        return False
