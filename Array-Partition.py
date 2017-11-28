
# Date: November 27, 2017
# Author: Oliver Jan
# Source: https://leetcode.com/problems/array-partition-i/description/

# PROBLEM STATEMENT
# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Input: [1,4,3,2]
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).


# Solution
class Solution(object):
    def array_pair_sum(nums):
        nums.sort()
        tol = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                tol += nums[i]
        return tol