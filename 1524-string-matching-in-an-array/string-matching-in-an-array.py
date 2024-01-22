from sortedcontainers import SortedSet
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=SortedSet()
        for i in words:
            for j in words:
                if i!=j and j in i:
                    ans.add(j)
        return list(ans)