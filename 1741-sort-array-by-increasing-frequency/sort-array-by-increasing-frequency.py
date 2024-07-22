class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d= Counter(nums).most_common()
        # d.sort(key=lambda x:x[0],reverse= True)
        # d.sort(key = lambda x:x[1])
        d.sort(reverse=True)
        d.sort(key = lambda x:x[1])
        l=[]
        for i in d:
            a,b=i
            for j in range(b):
                l.append(a)
        return l

