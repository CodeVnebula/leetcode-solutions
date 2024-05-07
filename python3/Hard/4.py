"""
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
    the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
"""
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        combined = sorted(nums1 + nums2)
        length = len(combined)
        return combined[length // 2] if length % 2 == 1 else (combined[length // 2 - 1] + combined[length // 2]) / 2
