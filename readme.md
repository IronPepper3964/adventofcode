# Advent of Code Repository

This code is my attempts to solve the Advent of Code puzzles, starting with 2025 (day 6).

## My Goals:
1. Solve all 2025 puzzles before the end of the year
2. Do not use AI unless I have solved the problem myself at least once
3. Solutions should be generalized as much as possible
    * Example - if the puzzle input file contains 3 rows of numbers, the code should be able to handle an arbitrary amount of rows and not rely on the file containing exactly 3 lists (unless the puzzle explicitly states a static number).

## Allowances:
1. Solutions do not need to be production grade.
2. Solutions do not need to be done in a 'normal' or best practice way
2. Documentation is optional
3. Error handling is optional (and generally expected to be skipped)

## Optional goals after completion:
* Complete previous years puzzles
* Cleanup existing solutions
    * Use best practices
    * Add Documentation
    * Improve approaches to solving the puzzles

# Current Progress
### 2025
``` text
*******...***...........

1   * *
2   * *
3   * *
4   * 
5   
6   * *
7   * 
8   
9   
10  
11  
12  
```
------------------

### Note about redundant code
Many (if not all) of the puzzles share common code.  

Normally I would move these to their own class/library to be reused.  However, to keep each puzzle solution 'self-contained', I opted to copy/paste the code into the puzzles that need them.  Generally I wanted someone to be able to view/run the entire puzzle solution using just a single file without external imports.

The most obvious example is my starting code for each puzzle which is readding in and cleaning up the puzzle file.  Really, that should be in it's own file to be reused by all the puzzles with say `aoc_helpers.read_puzzle_input(file_name)`