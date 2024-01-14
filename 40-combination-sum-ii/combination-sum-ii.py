class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        def find(ind, target):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(ind, len(c)):
                if i > ind and c[i] == c[i - 1]:
                    continue
                if c[i] > target:
                    break
                ds.append(c[i])
                find(i + 1, target - c[i])
                ds.pop()

        c.sort()
        ans = []
        ds = []
        ind = 0
        find(ind, target)
        return ans