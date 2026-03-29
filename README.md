# 20 Most-Asked DSA Questions in Coding Interviews

Solutions to the 20 most-frequently asked LeetCode-style Data Structures & Algorithms questions, implemented in **Java**, **C++**, and **Python**.

---

## 📂 Repository Structure

```
.
├── java/       # Java solutions (.java files, each file = one class)
├── cpp/        # C++ solutions (.cpp files, standalone programs)
└── python/     # Python solutions (.py files, standalone scripts)
```

Each solution file contains:
- Problem statement
- Chosen approach with explanation
- Time & Space complexity
- A `main` / `__main__` demo you can run directly

---

## 🗂️ Problem Index

### Category 1 — Arrays

| # | Problem | Approach | Time | Space |
|---|---------|----------|------|-------|
| 1 | [Two Sum](#1-two-sum) | HashMap (value → index) | O(n) | O(n) |
| 2 | [Maximum Subarray](#2-maximum-subarray) | Kadane's Algorithm | O(n) | O(1) |
| 3 | [Move Zeros](#3-move-zeros) | Two-pointer | O(n) | O(1) |
| 4 | [Best Time to Buy and Sell Stock](#4-best-time-to-buy-and-sell-stock) | Track min price | O(n) | O(1) |
| 5 | [Find Duplicate Number](#5-find-duplicate-number) | Floyd's Cycle Detection | O(n) | O(1) |

### Category 2 — Strings

| # | Problem | Approach | Time | Space |
|---|---------|----------|------|-------|
| 6 | [Valid Anagram](#6-valid-anagram) | Frequency count array | O(n) | O(1) |
| 7 | [Longest Substring Without Repeating Characters](#7-longest-substring-without-repeating-characters) | Sliding window + HashMap | O(n) | O(n) |
| 8 | [Longest Palindromic Substring](#8-longest-palindromic-substring) | Expand around center | O(n²) | O(1) |
| 9 | [String to Integer (atoi)](#9-string-to-integer-atoi) | Step-by-step parsing | O(n) | O(1) |

### Category 3 — Trees

| # | Problem | Approach | Time | Space |
|---|---------|----------|------|-------|
| 10 | [Maximum Depth of Binary Tree](#10-maximum-depth-of-binary-tree) | Recursive DFS | O(n) | O(h) |
| 11 | [Validate Binary Search Tree](#11-validate-binary-search-tree) | Min-max range recursion | O(n) | O(h) |
| 12 | [Level Order Traversal](#12-level-order-traversal) | BFS with queue | O(n) | O(n) |
| 13 | [Lowest Common Ancestor](#13-lowest-common-ancestor) | Post-order recursion | O(n) | O(h) |

### Category 4 — Binary Search

| # | Problem | Approach | Time | Space |
|---|---------|----------|------|-------|
| 14 | [Binary Search](#14-binary-search) | Classic binary search | O(log n) | O(1) |
| 15 | [Search in Rotated Sorted Array](#15-search-in-rotated-sorted-array) | Modified binary search | O(log n) | O(1) |

### Category 5 — Linked List

| # | Problem | Approach | Time | Space |
|---|---------|----------|------|-------|
| 16 | [Reverse Linked List](#16-reverse-linked-list) | Iterative pointer reversal | O(n) | O(1) |
| 17 | [Detect Cycle in Linked List](#17-detect-cycle-in-linked-list) | Floyd's slow-fast pointers | O(n) | O(1) |

### Category 6 — Sliding Window / Misc

| # | Problem | Approach | Time | Space |
|---|---------|----------|------|-------|
| 18 | [Longest Subarray with Sum K](#18-longest-subarray-with-sum-k) | Prefix sum + HashMap | O(n) | O(n) |
| 19 | [Subarray Sum Equals K](#19-subarray-sum-equals-k) | Prefix sum + frequency map | O(n) | O(n) |
| 20 | [Merge Intervals](#20-merge-intervals) | Sort + linear merge | O(n log n) | O(n) |

---

## 🔍 Problem Details

### 1. Two Sum

**Problem:** Given an array and a target, find the indices of two numbers that add up to the target.

**Approach:** Use a HashMap to store each number's index as we iterate. For every element, check if its complement (`target - element`) already exists in the map.

| Language | File |
|----------|------|
| Java     | `java/TwoSum.java` |
| C++      | `cpp/01_TwoSum.cpp` |
| Python   | `python/01_two_sum.py` |

---

### 2. Maximum Subarray

**Problem:** Find the contiguous subarray with the maximum sum.

**Approach (Kadane's Algorithm):** Maintain `currentSum`. If extending by the next element is worse than starting fresh, reset. Track `maxSum` throughout.

| Language | File |
|----------|------|
| Java     | `java/MaximumSubarray.java` |
| C++      | `cpp/02_MaximumSubarray.cpp` |
| Python   | `python/02_maximum_subarray.py` |

---

### 3. Move Zeros

**Problem:** Move all zeros to the end without changing the relative order of non-zero elements (in-place).

**Approach:** Two-pointer — `insertPos` tracks where the next non-zero element should go.

| Language | File |
|----------|------|
| Java     | `java/MoveZeros.java` |
| C++      | `cpp/03_MoveZeros.cpp` |
| Python   | `python/03_move_zeros.py` |

---

### 4. Best Time to Buy and Sell Stock

**Problem:** Given daily stock prices, find the maximum profit from a single buy-sell transaction.

**Approach:** Track the minimum price seen so far. At each step, compute potential profit and update the global maximum.

| Language | File |
|----------|------|
| Java     | `java/BestTimeToBuyAndSellStock.java` |
| C++      | `cpp/04_BestTimeToBuyAndSellStock.cpp` |
| Python   | `python/04_best_time_to_buy_and_sell_stock.py` |

---

### 5. Find Duplicate Number

**Problem:** Given an array of n+1 integers in range [1, n], find the duplicate without modifying the array and using O(1) extra space.

**Approach (Floyd's Cycle Detection):** Treat array values as "next" pointers in a linked list. The duplicate is the cycle entrance, found in two phases.

| Language | File |
|----------|------|
| Java     | `java/FindDuplicateNumber.java` |
| C++      | `cpp/05_FindDuplicateNumber.cpp` |
| Python   | `python/05_find_duplicate_number.py` |

---

### 6. Valid Anagram

**Problem:** Return true if two strings are anagrams of each other.

**Approach:** Frequency count array of size 26. Increment for the first string and decrement for the second. All counts must be zero.

| Language | File |
|----------|------|
| Java     | `java/ValidAnagram.java` |
| C++      | `cpp/06_ValidAnagram.cpp` |
| Python   | `python/06_valid_anagram.py` |

---

### 7. Longest Substring Without Repeating Characters

**Problem:** Find the length of the longest substring with no repeated characters.

**Approach:** Sliding window. Use a map to store the last-seen index of each character. Advance the left pointer past the duplicate when one is found.

| Language | File |
|----------|------|
| Java     | `java/LongestSubstringWithoutRepeatingCharacters.java` |
| C++      | `cpp/07_LongestSubstringWithoutRepeatingCharacters.cpp` |
| Python   | `python/07_longest_substring_without_repeating_characters.py` |

---

### 8. Longest Palindromic Substring

**Problem:** Find the longest palindromic substring in a string.

**Approach (Expand Around Center):** For each position, expand outward for both odd-length and even-length palindromes and track the longest.

| Language | File |
|----------|------|
| Java     | `java/LongestPalindromicSubstring.java` |
| C++      | `cpp/08_LongestPalindromicSubstring.cpp` |
| Python   | `python/08_longest_palindromic_substring.py` |

---

### 9. String to Integer (atoi)

**Problem:** Convert a string to a 32-bit signed integer, handling whitespace, optional sign, non-digit termination, and overflow.

**Approach:** Step through the string in order: skip whitespace → read sign → read digits → clamp to `[INT_MIN, INT_MAX]`.

| Language | File |
|----------|------|
| Java     | `java/StringToInteger.java` |
| C++      | `cpp/09_StringToInteger.cpp` |
| Python   | `python/09_string_to_integer.py` |

---

### 10. Maximum Depth of Binary Tree

**Problem:** Find the height (maximum depth) of a binary tree.

**Approach:** Recursive DFS — `depth = 1 + max(left depth, right depth)`.

| Language | File |
|----------|------|
| Java     | `java/MaximumDepthOfBinaryTree.java` |
| C++      | `cpp/10_MaximumDepthOfBinaryTree.cpp` |
| Python   | `python/10_maximum_depth_of_binary_tree.py` |

---

### 11. Validate Binary Search Tree

**Problem:** Determine if a binary tree is a valid BST.

**Approach:** Pass a `(min, max)` range down the recursion. Every node must satisfy `min < node.val < max`.

| Language | File |
|----------|------|
| Java     | `java/ValidateBST.java` |
| C++      | `cpp/11_ValidateBST.cpp` |
| Python   | `python/11_validate_bst.py` |

---

### 12. Level Order Traversal

**Problem:** Return the level-by-level (BFS) traversal of a binary tree.

**Approach:** Use a queue. For each level, iterate exactly `queue.size()` times and enqueue children for the next level.

| Language | File |
|----------|------|
| Java     | `java/LevelOrderTraversal.java` |
| C++      | `cpp/12_LevelOrderTraversal.cpp` |
| Python   | `python/12_level_order_traversal.py` |

---

### 13. Lowest Common Ancestor

**Problem:** Find the lowest common ancestor (LCA) of two nodes in a binary tree.

**Approach:** Post-order recursion. If both left and right subtrees return a match, the current node is the LCA.

| Language | File |
|----------|------|
| Java     | `java/LowestCommonAncestor.java` |
| C++      | `cpp/13_LowestCommonAncestor.cpp` |
| Python   | `python/13_lowest_common_ancestor.py` |

---

### 14. Binary Search

**Problem:** Search for a target in a sorted array and return its index (or -1).

**Approach:** Classic binary search — maintain `left` and `right` pointers, halve the search space each iteration.

| Language | File |
|----------|------|
| Java     | `java/BinarySearch.java` |
| C++      | `cpp/14_BinarySearch.cpp` |
| Python   | `python/14_binary_search.py` |

---

### 15. Search in Rotated Sorted Array

**Problem:** Search for a target in a sorted array that has been rotated at an unknown pivot.

**Approach:** Modified binary search. Determine which half is sorted at every step, then decide which half the target must lie in.

| Language | File |
|----------|------|
| Java     | `java/SearchInRotatedSortedArray.java` |
| C++      | `cpp/15_SearchInRotatedSortedArray.cpp` |
| Python   | `python/15_search_in_rotated_sorted_array.py` |

---

### 16. Reverse Linked List

**Problem:** Reverse a singly linked list in-place.

**Approach (Iterative):** Maintain `prev` and `curr` pointers. Re-link each node to point backward, then advance both pointers.

| Language | File |
|----------|------|
| Java     | `java/ReverseLinkedList.java` |
| C++      | `cpp/16_ReverseLinkedList.cpp` |
| Python   | `python/16_reverse_linked_list.py` |

---

### 17. Detect Cycle in Linked List

**Problem:** Determine if a linked list contains a cycle.

**Approach (Floyd's Cycle Detection):** Use a slow pointer (1 step) and a fast pointer (2 steps). If they ever meet, a cycle exists.

| Language | File |
|----------|------|
| Java     | `java/DetectCycleInLinkedList.java` |
| C++      | `cpp/17_DetectCycleInLinkedList.cpp` |
| Python   | `python/17_detect_cycle_in_linked_list.py` |

---

### 18. Longest Subarray with Sum K

**Problem:** Find the length of the longest contiguous subarray whose sum equals K (array may contain negatives).

**Approach:** Prefix sum + HashMap. Store the earliest index where each prefix sum occurred. If `(prefixSum - K)` has been seen, we have a valid subarray.

| Language | File |
|----------|------|
| Java     | `java/LongestSubarrayWithSumK.java` |
| C++      | `cpp/18_LongestSubarrayWithSumK.cpp` |
| Python   | `python/18_longest_subarray_with_sum_k.py` |

---

### 19. Subarray Sum Equals K

**Problem:** Count the total number of subarrays whose sum equals K.

**Approach:** Prefix sum + frequency map. For each index, count how many past prefix sums equal `(prefixSum - K)`.

| Language | File |
|----------|------|
| Java     | `java/SubarraySumEqualsK.java` |
| C++      | `cpp/19_SubarraySumEqualsK.cpp` |
| Python   | `python/19_subarray_sum_equals_k.py` |

---

### 20. Merge Intervals

**Problem:** Given a list of intervals, merge all overlapping intervals.

**Approach:** Sort intervals by start time. Iterate and extend the last merged interval when the next one overlaps; otherwise append.

| Language | File |
|----------|------|
| Java     | `java/MergeIntervals.java` |
| C++      | `cpp/20_MergeIntervals.cpp` |
| Python   | `python/20_merge_intervals.py` |

---

## ▶️ How to Run

### Python
```bash
python3 python/01_two_sum.py
```

### Java
```bash
javac java/TwoSum.java -d out/
java -cp out/ TwoSum
```

### C++
```bash
g++ -std=c++17 -o two_sum cpp/01_TwoSum.cpp
./two_sum
```

---

## 📌 Notes

- All solutions follow the LeetCode constraints and method signatures.
- Each file is self-contained and runnable independently.
- `h` in space complexities refers to the height of the tree (O(log n) for balanced, O(n) worst-case).
