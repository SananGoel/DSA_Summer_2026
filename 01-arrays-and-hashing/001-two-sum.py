"""
LeetCode 1 — Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: Arrays & Hashing (complement lookup)

Problem:
Given an array of integers nums and an integer target, return the indices
of the two numbers such that they add up to target. Each input has exactly
one solution, and you may not use the same element twice.

Approach 1 — Brute force (nested loops):
- Define two pointers
- Start checking each pair by fixing one pointer and moving the other 
- If the sum of both pointers equals the target return the indices 
- Continue by incrementing the fixed pointer by 1 till it reaches the end 
of the list 

Approach 2 — Hash map / complement lookup (optimal):
- For each number, compute its complement (target - num)
- Check if the complement is already in our dict
- If yes, we found the pair → return the stored index and current index
- If no, store the current number → continue
- Key insight: trade memory for time. Instead of searching for the pair
  by checking every other element (O(n) per element), we store what we've
  seen and look up the complement in O(1).]

Why overwriting in the dict is safe:
If a valid pair exists, we'd find it on the
check step before we ever overwrite. Also, the problem doesn't require
smallest-index pairs, just any valid pair.

Complexity:
- Approach 1: O(n²) time, O(1) space
- Approach 2: O(n) time, O(n) space (the dict can hold up to n entries)
"""


class Solution:
    # Approach 1: Brute force
    def twoSum_brute(self, nums: list[int], target: int) -> list[int]:
        pointer1 = 0
        while pointer1 < len(nums):
            pointer2 = pointer1 + 1
            while pointer2 < len(nums):
                if nums[pointer1] + nums[pointer2] == target:
                    return [pointer1, pointer2]
                pointer2 += 1
            pointer1 += 1

    # Approach 2: Hash map (optimal)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mydict = {}
        for index, number in enumerate(nums):
            number_to_find = target - number
            if number_to_find in mydict:
                return [mydict[number_to_find], index]
            mydict[number] = index
