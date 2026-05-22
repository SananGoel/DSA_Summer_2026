"""
LeetCode 347 — Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Pattern: Arrays & Hashing (counting + sorting by value)

Problem:
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Approach — count + sort by frequency:
- Build a frequency dict mapping each number to how many times it appears
- Sort the (number, count) pairs by count, descending
- Take the first k pairs and extract just the numbers

The lambda key:
sorted(..., key=lambda x: x[1]) tells Python "for each pair x, sort by
x[1] (the count) instead of x[0] (the number itself)." reverse=True flips
it to descending so the highest counts come first.

The list comprehension:
[pair[0] for pair in sorted_keys[:k]] means "iterate over the first k pairs
and grab the number (index 0) from each one."

Complexity:
- Time: O(n log n) — dominated by sorting the unique elements
- Space: O(n) — dict can hold up to n unique numbers

Future optimization (not implemented):
A bucket sort approach solves this in O(n) by creating n+1 buckets indexed
by frequency and scanning from highest to lowest. Skipping for now since
O(n log n) is accepted and simpler to reason about.
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mydict = {}
        for number in nums:
            mydict[number] = mydict.get(number, 0) + 1
        sorted_keys = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        ans = [pair[0] for pair in sorted_keys[:k]]
        return ans
