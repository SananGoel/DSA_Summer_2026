"""
LeetCode 242 — Valid Anagram
https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Pattern: Arrays & Hashing

Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Approach 1 — Sorting (the "easy" answer):
Just sort both strings, it return a list with sorted characters and check if they are the same. 

Approach 2 — Hash map counting (the optimal answer):
We use dictionaries to keep a track of all characters in s and t, if both dictionaries are equal, we return True else False.

Why approach 2 is better:
This is optimal as sorting takes O(nlogn) while this solution is O(n+n) = O(n) 


Complexity:
- Approach 1: O(n log n) time, O(n) space (sorting)
- Approach 2: O(n) time, O(1) space (only 26 possible letters)
"""


class Solution:
    # Approach 1: Sorting
    def isAnagram_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # Approach 2: Hash map counting (optimal)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        return count_s == count_t
