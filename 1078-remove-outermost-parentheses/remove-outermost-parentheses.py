class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        # l.append(0)
        s=list(s)
        for i in range(len(s)):
            if s[i]=="(":
                if c==0:
                    s[i]=""
                c+=1
            else:
                c-=1
            if c==0:
                s[i]=""
        return "".join(s)


        