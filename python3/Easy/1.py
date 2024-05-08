""" 
    Given an array of integers nums and an integer target, return indices of the 
    two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you 
    may not use the same element twice.

    You can return the answer in any order.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}  
        # Using caching approach
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
