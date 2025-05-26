# Leetcode 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

"""
Approach: Merge Sorted Array using optimal reverse two-pointer approach
Time Complexity: O(m +1 n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_length = m+n
        num1_right_index, num2_right_index = m-1, n-1
        insert_index = total_length-1
        while(num1_right_index >= 0 and num1_right_index < total_length and num2_right_index >= 0 and num2_right_index < total_length ):
            if nums1[num1_right_index] < nums2[num2_right_index]:
                nums1[insert_index] = nums2[num2_right_index]
                insert_index-=1
                num2_right_index-=1
            else:
                nums1[insert_index] = nums1[num1_right_index]
                nums1[num1_right_index] = 0
                insert_index-=1
                num1_right_index-=1
        
        for index, rest_element in enumerate(nums2[:num2_right_index+1], start=0):
            nums1[index] = rest_element

# instance = Solution()
# print(instance.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5))