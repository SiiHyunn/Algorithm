class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        
        quotient = len(nums1) // 2
        remainder = len(nums1) % 2
        
        if remainder == 0:
            median = float((nums1[quotient-1]+nums1[quotient])) /2
        else:
            median = float(nums1[quotient])
            
        return median