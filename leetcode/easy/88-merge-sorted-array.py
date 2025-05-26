# Leetcode 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

"""
Approach: Two-pointer from the back
Time Complexity: O(m * n)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_length = m+n
        num1_left_index, num2_left_index = 0, 0
        while(num1_left_index < total_length and num2_left_index < n):
            if nums1[num1_left_index] <= nums2[num2_left_index]:
                num1_left_index+=1
            else:
                nums1.insert(num1_left_index, nums2[num2_left_index])
                nums1.pop()
                num2_left_index+=1
        #Track last index 
        last_index = total_length-(n-num2_left_index)
        for index, rest_element in enumerate(nums2[num2_left_index:], start=last_index):
            nums1[index] = rest_element
        # print(nums1)
# instance = Solution()
# print(instance.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5))