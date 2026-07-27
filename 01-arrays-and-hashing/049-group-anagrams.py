"""
LeetCode 49 — Group Anagrams
https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Pattern: Arrays & Hashing (canonical key grouping)

Problem:
Given an array of strings strs, group the anagrams together. You can
return the answer in any order. An anagram is a word formed by
rearranging the letters of another, using all original letters exactly
once.

Approach — sorted string as a canonical key:
- Two words are anagrams if and only if they contain the exact same
  letters, just in a different order
- Sorting a word's letters gives a "fingerprint" that's identical for
  all its anagrams: sorted("eat") == sorted("tea") == sorted("ate")
- Use that sorted string as a dict key, and map it to a list of all
  original words that share that key
- At the end, the dict's values are exactly the groups we want

Approach 1 — manual dict with if/else:
- For each word, compute key = "".join(sorted(word))
- If key isn't in the dict yet, start a new list: dict[key] = [word]
- If key already exists, append to the existing list
- Same "check before insert" pattern as Two Sum's complement lookup

Approach 2 — defaultdict(list) (cleaner):
- defaultdict(list) auto-creates an empty list the first time a new
  key is accessed, so the if/else check collapses into one line:
  groups[key].append(word)
- Behaviorally identical to Approach 1, just less boilerplate

Complexity (both approaches):
- Time: O(n * m log m) — n words, each of length up to m, and sorting
  each word costs O(m log m)
- Space: O(n * m) — storing all words/keys across the dict
"""
from collections import defaultdict


class Solution:
    # Approach 1: manual dict with if/else
    def groupAnagrams_manual(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return [""]
        mydict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in mydict:
                mydict[key] = [word]
            else:
                mydict[key].append(word)
        return list(mydict.values())

    # Approach 2: defaultdict(list) (cleaner)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return [""]
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
