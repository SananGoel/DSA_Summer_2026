"""
LeetCode 128 — Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium
Pattern: Arrays & Hashing (set lookup + sequence-start detection)

Problem:
Given an unsorted array of integers nums, return the length of the
longest consecutive elements sequence. Must run in O(n) time.

Approach 1 — count forward from every element (looks similar, but O(n^2)):
- Put all numbers in a set for O(1) lookup
- For every number i in nums, walk forward (i+1, i+2, ...) counting how
  far the consecutive run extends, and track the max count seen
- The flaw: there's no check for whether i is the START of a sequence.
  For a long run like [1,2,3,...,1000], this walks forward from EVERY
  single number in the run, re-counting the same run over and over
  (once from 1, again from 2, again from 3, ...). That's O(n) work
  triggered by each of the n elements -> O(n^2) worst case
- It can still pass on LeetCode with a fast runtime, because the given
  test cases may not include a single run long enough to expose the
  quadratic blowup — a fast submission time doesn't guarantee optimal
  complexity

Approach 2 — only start counting from true sequence starts (optimal):
- Same set lookup, but add one guard: only begin counting forward from
  i if (i - 1) is NOT in the set
- If (i - 1) IS in the set, i is somewhere in the middle of a sequence,
  and whichever number actually starts that sequence will already walk
  through the entire run — recounting from the middle is redundant
- This guarantees every number is only ever the start of at most one
  counted walk, since a number can't be the start of two different
  sequences
- Because of that guarantee, the total number of "while" steps summed
  across every iteration of the outer loop adds up to at most n —
  each element gets walked over exactly once, by whichever number
  happens to be its sequence's true start. That's what makes this
  version genuinely O(n)

Complexity:
- Approach 1: O(n^2) worst case (long consecutive runs get re-walked
  from every element inside them), O(n) space for the set. 
  For example: if nums = [1,2,3,....1000], the code tries to find next_num 
  for each number: first it goes through 1-1000, then 2-1000 and so on..
- Approach 2: O(n) time (each element is walked at most once total,
  across the whole run of the algorithm), O(n) space for the set
"""


class Solution:
    # Approach 1: count forward from every element (looks similar, but O(n^2))
    def longestConsecutive_bruteish(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        ans_count = 1

        for i in nums:
            count = 1
            next_num = i + 1
            while next_num in nums_set:
                count += 1
                next_num += 1
            ans_count = max(count, ans_count)

        return ans_count

    # Approach 2: only start counting from true sequence starts (optimal)
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        ans_count = 1

        for i in nums:
            if i - 1 not in nums_set:
                count = 1
                next_num = i + 1
                while next_num in nums_set:
                    count += 1
                    next_num += 1
                ans_count = max(count, ans_count)

        return ans_count
