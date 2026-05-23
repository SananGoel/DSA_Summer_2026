"""
LeetCode 271 / NeetCode "Encode and Decode Strings"
https://neetcode.io/problems/string-encode-and-decode
Difficulty: Medium
Pattern: String parsing with length-prefix framing

Problem:
Design encode and decode functions. encode takes a list of strings and
returns a single string. decode reverses that single string back into
the original list. Strings can contain ANY characters, so delimiter-only
approaches don't work.

Key insight — length-prefix framing:
Instead of relying on a special delimiter to separate strings, prefix
each string with its length followed by a marker (#). Decode reads the
length first, then grabs exactly that many characters as the string.
The string's content is read by counting, not by scanning — so the
content can include any character including # without confusion.

This is the same technique used in HTTP (Content-Length headers), TCP
framing, Protocol Buffers, and most binary file formats.

---

Approach 1 — Initial attempt (character-by-character with slicing):
[walked through s one or two chars at a time,
mutated s by slicing, handled multi-digit lengths with a separate branch.
Works but is O(n²) because every slice copies the rest of the string.]

Approach 2 — Index-pointer (cleaner, O(n)):
[use index i to walk through s. For each
iteration, walk j forward until s[j] == "#" to find the length, parse it,
slice out the next `length` chars as the word, then jump i forward past
everything we just consumed. No string mutation, single pass.]

Why approach 2 is better:
[O(n) vs O(n²) because no copying. Cleaner logic — one branch
instead of three. The "two pointers walking through a string" pattern
generalizes to lots of other problems.]

Complexity:
- Approach 1: O(n²) time, O(n) space (slicing creates new strings)
- Approach 2: O(n) time, O(n) space (single pass, no mutation)
"""


class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

    # Approach 1: original attempt (works but O(n²))
    def decode_v1(self, s: str) -> list[str]:
        lst = []
        while s:
            prev = s[0]
            nxt = s[1]
            if nxt == "#" and prev.isdigit():
                element = s[2:2+int(prev)]
                lst.append(element)
                s = s[2+int(prev):]
            elif prev.isdigit() and nxt.isdigit():
                prev = prev + nxt
                s = s[2:]
                char = s[0]
                while char != "#":
                    prev = prev + char
                    s = s[1:]
                    char = s[0]
                element = s[1:1+int(prev)]
                lst.append(element)
                s = s[1+int(prev):]
        return lst

    # Approach 2: index-pointer (cleaner, O(n))
    def decode(self, s: str) -> list[str]:
        i = 0
        lst = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            lst.append(word)
            i = j + 1 + length
        return lst
