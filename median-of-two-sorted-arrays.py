class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_array= sorted(nums1 + nums2)
        merge_length = len(merged_array)
        int_part = int(merge_length//2)
        if merge_length%2 == 0:
            return (merged_array[int_part-1] + merged_array[int_part])/2.0
        return merged_array[int_part]