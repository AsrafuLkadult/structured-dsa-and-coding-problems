# Leetcode 2894. divisible-and-non-divisible-sums-difference
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

"""
Approach: Loop from 1 to n, summing values based on whether each is divisible by m or not.
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1 = sum([element for element in range(1, n+1) if element % m != 0])
        num2 = sum([element for element in range(1, n+1) if element % m == 0])
        return num1-num2

# instance = Solution()
# print(instance.differenceOfSums(10, 3))