class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if (len(nums1)+len(nums2))%2 == 0:
            
            return (sorted(nums1+nums2)[(len(nums1)+len(nums2))//2] + sorted(nums1+nums2)[(len(nums1)+len(nums2))//2 -1]) / 2
        
        
        return sorted(nums1+nums2)[(len(nums1)+len(nums2))//2]