class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        
        res.sort()
        if len(res) >=3:
            return res[-3]
        else:
            return res[-1]
