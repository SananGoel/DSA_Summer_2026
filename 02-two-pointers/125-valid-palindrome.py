"""
LeetCode 125 — Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Pattern: Two Pointers (skip non-alphanumeric, compare case-insensitively)

Problem:
Given a string s, return true if it is a palindrome after converting all
uppercase letters to lowercase and removing all non-alphanumeric
characters. An empty string is considered a valid palindrome.

Approach 1 — two pointers with 4 explicit branches:
- pointer1 starts at index 0, pointer2 starts at the last index
- While pointer1 <= pointer2, check every combination of "is
  s[pointer1] alnum" and "is s[pointer2] alnum":
    - left alnum, right not alnum -> skip right (pointer2 -= 1)
    - left not alnum, right alnum -> skip left (pointer1 += 1)
    - neither alnum -> skip both
    - both alnum -> compare .lower() versions; return False on mismatch,
      otherwise advance both pointers inward
- Works correctly, but requires reasoning through 4 separate branches
  to convince yourself every case is handled

Approach 2 — two pointers with separate skip-loops (cleaner):
- Same two pointers, but instead of branching on every alnum
  combination, use two small inner while loops:
    - nudge pointer1 forward while it's sitting on a non-alnum char
    - nudge pointer2 backward while it's sitting on a non-alnum char
- After skipping, check if the pointers crossed (pointer1 > pointer2)
  during the skips — if so, there's nothing left to compare, so break
- Otherwise compare s[pointer1] and s[pointer2] case-insensitively;
  return False on mismatch, else advance both pointers inward
- Only one real comparison branch instead of four — same job, less
  branching to reason about

A note on the crossed-pointer edge case:
- The inner skip-loops each guard with "pointer1 <= pointer2" so they
  don't run forever, but that guard only prevents ANOTHER iteration —
  it can't undo a pointer move that already happened. So it's possible
  for the skip-loops to leave pointer1 > pointer2 by the time they
  finish (e.g. skipping trailing junk causes the pointers to cross).
  Without an explicit check for that after the skip-loops, the next
  line would try to index a position that's no longer valid, causing
  an IndexError. Both approaches below handle this correctly.

Why nested-looking loops here are still O(n), not O(n^2):
- It looks like "two while loops, one inside the other" should be
  O(n^2), but that's only true when the inner loop's work resets and
  repeats in full on every outer iteration (classic nested-loop
  blowup). Here, pointer1 and pointer2 are shared across every
  iteration and never reset — each pointer can only move in one
  direction, and never revisits a position it already passed.
- Think of it as a shared, shrinking budget: pointer1 can move forward
  at most n times total across the ENTIRE run of the function (from
  index 0 to at most index n-1), and pointer2 can move backward at
  most n times total, no matter which loop (skip-loop or the final
  advance) is the one doing the moving.
- So the grand total of all pointer movements, summed across every
  outer iteration and every inner skip-loop call combined, is capped
  at roughly 2n — not n per outer iteration. This is amortized
  analysis: look at the total work available across the whole run,
  not "worst case per outer iteration, multiplied out."

Complexity (both approaches):
- Time: O(n) — amortized, as explained above; each character is
  visited/skipped a bounded number of times across the whole run
- Space: O(1) — only two integer pointers, no extra data structures
"""


class Solution:
    # Approach 1: two pointers with 4 explicit branches
    def isPalindrome_branching(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer1 <= pointer2:
            if (s[pointer1]).isalnum() and not (s[pointer2]).isalnum():
                pointer2 -= 1
                continue
            elif not (s[pointer1]).isalnum() and (s[pointer2]).isalnum():
                pointer1 += 1
                continue
            elif not (s[pointer1]).isalnum() and not (s[pointer2]).isalnum():
                pointer1 += 1
                pointer2 -= 1
                continue
            if (s[pointer1]).lower() == (s[pointer2]).lower():
                pointer1 += 1
                pointer2 -= 1
                continue
            else:
                return False
        return True

    # Approach 2: two pointers with separate skip-loops (cleaner)
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer1 <= pointer2:
            while pointer1 <= pointer2 and not s[pointer1].isalnum():
                pointer1 += 1
            while pointer1 <= pointer2 and not s[pointer2].isalnum():
                pointer2 -= 1

            if pointer1 <= pointer2:
                if s[pointer1].lower() != s[pointer2].lower():
                    return False

            pointer1 += 1
            pointer2 -= 1

        return True
