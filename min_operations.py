class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if (i=='../'):
                if count == 0:
                    count = 0
                else:
                    count-=1
            elif( i == './'):
                count = count
            else:
                count +=1
        
        return count
        
