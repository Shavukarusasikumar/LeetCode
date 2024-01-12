class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        i,j=0,len(s)-1
        k=j//2
        c1,c2=0,0
        while i<=k:
            if s[i]=='a' or s[i]=="e" or s[i]=='i' or s[i]=="o" or s[i]=="u":
                c1+=1
            if s[j]=='a' or s[j]=="e" or s[j]=='i' or s[j]=="o" or s[j]=="u":
                c2+=1
            i+=1
            j-=1
        return c1==c2
