"""
LeetCode 167 — Two Integer Sum II (Two Sum II - Input Array Is Sorted)
https://neetcode.io/problems/two-integer-sum-ii
Difficulty: Medium
Pattern: Two Pointers (sorted array, narrow from both ends)

Problem:
Given an array of integers numbers sorted in non-decreasing order,
return the indices (1-indexed) of two numbers, [index1, index2], such
that they add up to a given target, with index1 < index2. There is
always exactly one valid solution. The solution must use O(1)
additional space.

Approach — two pointers narrowing from both ends:
- left starts at index 0 (smallest value), right starts at the last
  index (largest value)
- While left < right, compute currentsum = numbers[left] + numbers[right]
- If currentsum < target, the sum is too small -> move left forward
  (only increasing numbers[left] can increase the sum, since the array
  is sorted ascending)
- If currentsum > target, the sum is too big -> move right backward
  (only decreasing numbers[right] can decrease the sum)
- If currentsum == target, return the answer as 1-indexed positions:
  [left + 1, right + 1]

Why this only works because the array is sorted:
- Sortedness is what guarantees moving left forward can only increase
  the sum, and moving right backward can only decrease it. That
  guarantee is what makes narrowing from both ends correct instead of
  arbitrary — without sortedness there'd be no way to know which
  direction to move.

Comparison with the original Two Sum (unsorted array, no space limit):
- Two Sum's optimal approach is a hash map / complement lookup, since
  there's no ordering to exploit and O(n) space is allowed
- Here, the array is already sorted AND the problem explicitly requires
  O(1) additional space, which rules out a hash map entirely
- Same problem shape, but the extra piece of information (sorted input)
  unlocks a completely different, more space-efficient technique — a
  hash-map solution generalizes to unsorted data, but sorted input is
  almost always a strong signal to try two pointers instead, trading
  O(n) space for O(1) space by exploiting the order

Complexity:
- Time: O(n) — left and right only ever move toward each other, so the
  total number of steps across the whole run is bounded by n
- Space: O(1) — only two integer pointers, no extra data structures
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            currentsum = numbers[left] + numbers[right]

            if currentsum < target:
                left += 1
            elif currentsum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
