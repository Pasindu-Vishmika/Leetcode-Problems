
# Runtime =>    69 ms       Beats 51.22% of users with Python3
# Memory  =>    17.63 MB    Beats 72.98% of users with Python3


class Solution:
    def twoSum(self, nums, target):
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indices:
                return [num_indices[complement], i]
            
            num_indices[num] = i
        
        return []