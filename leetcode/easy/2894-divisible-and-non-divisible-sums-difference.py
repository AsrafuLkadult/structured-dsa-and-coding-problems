# Leetcode 2894. divisible-and-non-divisible-sums-difference
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

"""
Approach: sum of natural number law n*(n+1) //2 
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        if m == 1:
            return 0 - (n*(n+1) //2)   # Special case
        total_sum = n*(n+1) // 2
        multiples_count = n // m  # number of multiples of m up to n
        num2 = (multiples_count*(multiples_count+1) // 2)*m
        num1 = total_sum - num2  # Not divisible sum 
        return num1-num2

instance = Solution()
print(instance.differenceOfSums(15, 9))