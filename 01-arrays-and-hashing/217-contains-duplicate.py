"""
LeetCode 217 — Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Pattern: Arrays & Hashing

Problem:
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.

Approach:
Just keep track of what you see in a set named seen. If you stumble upon something in seen return true else return False

Why a set?
Lookup time for a set is O(1) because it uses hash tables in the background, and doesnt have a value associated with a key like in a dictionary, hence we use sets

Complexity:
- Time: O(n) — single pass through the array
- Space: O(n) — set can hold up to n elements in the worst case
"""


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
