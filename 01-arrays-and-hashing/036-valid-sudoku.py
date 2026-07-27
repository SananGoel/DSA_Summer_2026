"""
LeetCode 36 — Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
Difficulty: Medium
Pattern: Arrays & Hashing (set-based duplicate detection across overlapping groups)

Problem:
Given a 9x9 Sudoku board, determine if it is valid according to these
rules only (the board does not need to be solvable or full):
1. Each row must contain digits 1-9 without duplicates
2. Each column must contain digits 1-9 without duplicates
3. Each of the nine 3x3 sub-boxes must contain digits 1-9 without
   duplicates
Empty cells are represented by '.' and should be ignored when checking
for duplicates.

Approach 1 — three separate full passes (rows, then columns, then boxes):
- isRowValid(row_number): walk across one row, track seen digits in a
  set, return False on a repeat
- isColumnValid(column_number): same idea, walking down one column
- isBoxValid(box_number): same idea, walking a 3x3 box
- Box indexing: start = (box_number // 3) * 3 gives the row-group start,
  start2 = (box_number % 3) * 3 gives the column-group start. E.g.
  box_number=4 -> start=3, start2=3 -> rows 3-5, cols 3-5 (middle box)
- Main loop calls all three checks for i in range(9) and short-circuits
  to False the moment any one fails
- Each cell in the board ends up visited 3 separate times (once per
  check, each triggered once per row/col/box index), across 3 separate
  function calls

Approach 2 — single pass with three simultaneous trackers (cleaner):
- Walk every cell (r, c) exactly once
- Maintain rows[r], cols[c], and boxes[(r//3, c//3)] as sets of digits
  seen so far in that row/column/box
- (r // 3, c // 3) is a neat trick: r//3 gives "which row-third" (0,1,2)
  and c//3 gives "which column-third" (0,1,2); together they uniquely
  identify one of the 9 boxes without needing a separate box_number
  loop variable at all
- For each cell, check membership in all three sets at once; if the
  digit is already in any of them, return False immediately
- Otherwise add the digit to all three sets and continue
- defaultdict(set) auto-creates an empty set the first time a new
  row/col/box key is touched, same trick as defaultdict(list) in Group
  Anagrams, just with a different container

Why Approach 2 is preferred:
- Every cell is visited exactly once instead of three times
- No redundant re-derivation of row/column/box slices across separate
  function calls
- Considered the canonical/idiomatic solution for this problem

Note on complexity:
- The board size is fixed at 9x9 (81 cells, 9 rows, 9 cols, 9 boxes),
  so both approaches are O(1) time and O(1) space in the strict
  Big-O sense — the input size never grows. Approach 2's benefit is a
  smaller constant factor (fewer total cell visits), not a better
  asymptotic class. The advantage would become more visible on a
  variable-size grid (e.g. 16x16), where 3 separate passes do
  noticeably more redundant work than 1 combined pass.
"""
from collections import defaultdict


class Solution:
    # Approach 1: three separate full passes (rows, then columns, then boxes)
    def isValidSudoku_threePass(self, board: list[list[str]]) -> bool:
        def isRowValid(row_number):
            seen = set()
            for index in range(0, 9):
                if board[row_number][index] in seen:
                    return False
                elif (board[row_number][index]).isnumeric():
                    seen.add(board[row_number][index])
            return True

        def isColumnValid(column_number):
            seen = set()
            for row_number in range(0, 9):
                if board[row_number][column_number] in seen:
                    return False
                elif (board[row_number][column_number]).isnumeric():
                    seen.add(board[row_number][column_number])
            return True

        def isBoxValid(box_number):
            seen = set()
            start = (box_number // 3) * 3
            start2 = (box_number % 3) * 3
            for row in range(start, start + 3):
                for j in range(start2, start2 + 3):
                    if board[row][j] in seen:
                        return False
                    elif (board[row][j]).isnumeric():
                        seen.add(board[row][j])
            return True

        is_valid = True
        for i in range(0, 9):
            if not isRowValid(i) or not isColumnValid(i) or not isBoxValid(i):
                is_valid = False
        return is_valid

    # Approach 2: single pass with three simultaneous trackers (cleaner)
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_id = (r // 3, c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True
