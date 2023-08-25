class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start = 0
        end = 0
        cur_sum = 0
        min_length = float('inf')

        if sum(nums) < target:
            return 0
        
        for end in range(len(nums)):
            cur_sum += nums[end]
            end +=1

            while start < end and cur_sum >= target:  
                cur_sum = cur_sum - nums[start]
                start = start + 1

                min_length = min(min_length, end-start+1) 

        return min_length
