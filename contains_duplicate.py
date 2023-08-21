class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict= {}
        
        for i in nums:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1

        
        for count in dict.values():
             if count>1:
                 return True
        
        return False
