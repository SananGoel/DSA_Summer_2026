"""
LeetCode 238 — Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Pattern: Arrays & Hashing (prefix / suffix product)

Problem:
Given an integer array nums, return an array output where output[i] is
the product of all the elements of nums except nums[i]. Each product is
guaranteed to fit in a 32-bit integer. Must be solved without using
division, ideally in O(n) time.

Approach — prefix (left) and suffix (right) product arrays:
- For any index i, "product of everything except nums[i]" is exactly
  (product of everything to the LEFT of i) * (product of everything to
  the RIGHT of i)
- Build left[i] = product of all elements before index i
- Build right[i] = product of all elements after index i
- Answer at index i is just left[i] * right[i]
- This avoids division entirely, which also sidesteps the zero-in-array
  problem that a divide-based approach would hit

Building left:
- left[0] = 1 (nothing exists before index 0, so the identity product is 1)
- left[i] = left[i-1] * nums[i-1], walking left to right

Building right:
- right[-1] = 1 (nothing exists after the last index)
- right[i] = right[i+1] * nums[i+1], walking right to left
- Current implementation uses right.insert(0, ...) while walking
  backward, which is correct but O(n) per insert (shifts the whole
  list), making the overall right-array build O(n^2). A cleaner O(n)
  version pre-sizes right = [1] * len(nums) and fills by index
  assignment instead of insert(0, ...) — noted as a future cleanup,
  not implemented here since correctness isn't affected.

Combining:
- Walk through every index and multiply left[i] * right[i] to get the
  final answer array

Complexity:
- Time: O(n^2) as currently written (due to right.insert(0, ...));
  O(n) achievable with index-assignment instead of insert
- Space: O(n) — left, right, and the output list each hold n elements
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = [1]
        right = [1]
        lst = []

        for i in range(1, len(nums)):
            left.append(left[i-1] * nums[i-1])

        for i in range(len(nums)-1, 0, -1):
            right.insert(0, (right[0] * nums[i]))

        for i in range(len(left)):
            lst.append(left[i] * right[i])

        return lst
