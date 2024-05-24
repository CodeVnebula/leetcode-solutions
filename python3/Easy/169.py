""" 
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        same_num_counts = {}
        
        for num in nums:
            if num not in same_num_counts:
                same_num_counts[num] = 1
            else:
                same_num_counts[num] += 1
        
        n = n // 2
        for key, value in same_num_counts.items():
            if value > n:
                return key
