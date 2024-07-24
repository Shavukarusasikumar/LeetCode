class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def fun(n):
            temp=[]
            for i in str(n):
                temp.append(int(i))
            return temp
        temp=[]
        for val in nums:
            k=fun(val)
            d=0
            for i in k:
                d=d*10+mapping[i]
            temp.append((val,d))
        sorted_temp=sorted(temp,key=lambda item:item[1])
        sorted_val=[i[0] for i in sorted_temp]
        return sorted_val