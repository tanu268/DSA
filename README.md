# LeetCode DSA Practice (Beginner to Advanced)

Welcome to my LeetCode practice repository!  
Here, I solve Data Structures and Algorithms problems from scratch—starting with brute-force, then moving on to better and optimal solutions.  
This journey is designed to help **beginners** understand how to approach DSA problems step-by-step.

---

## 📁 Folder Structure

Each problem is saved in the format:


For example:
- `03_rotate_array_bt.py` → Better
- `05_missing_number_op2.py` → Optimal (XOR-based)

---

## Problem Details and Approaches

### 01. Sorted and Rotated Array

- 🔢 Files: `01_sorted_and_rotated_bf.py`, `01_sorted_and_rotated_op.py`

- 🚶 Brute Force:
  - Try all possible rotations and check if any is sorted.
  - ✅ Good for understanding rotation mechanics.

- ⚡ Optimal:
  - Count how many times `arr[i] > arr[i+1]` — only one such drop allowed.
  - ✅ O(n) check without full rotation.

---

### 02. Remove Duplicates from Sorted Array

- 🔢 Files: `02_remove_duplicates_bf.py`, `02_remove_duplicates_op.py`

- 🚶 Brute Force:
  - Store unique values in a new list.
  - ✅ Easy to implement but uses extra space.

- ⚡ Optimal:
  - Two pointers to overwrite duplicates in-place.
  - ✅ Interview-favorite in-place pattern.

---

### 03. Rotate Array

- 🔢 Files: `03_rotate_array_bf.py`, `03_rotate_array_bt.py`, `03_rotate_array_op.py`

- 🚶 Brute Force:
  - Rotate the array one step at a time, `k` times.
  - ❌ Inefficient for large arrays.

- 🔁 Better:
  - Use extra array and copy elements directly to correct position.
  - ✅ O(n) time but O(n) space.

- ⚡ Optimal:
  - Reverse the whole array, then reverse parts.
  - ✅ O(n) time, O(1) space — elegant trick.

---

### 04. Move Zeroes

- 🔢 Files: `04_move_zeroes_bf.py`, `04_move_zeroes_bt.py`, `04_move_zeroes_op.py`

- 🚶 Brute Force:
  - Store all non-zeroes, then append zeroes.
  - ✅ Simple, but not in-place.

- 🔁 Better:
  - Count and shift values manually.
  - ✅ Less extra space.

- ⚡ Optimal:
  - Two-pointer in-place swap of zero and non-zero.
  - ✅ Best in time and space.

---

### 05. Missing Number

- 🔢 Files: `05_missing_number_bf.py`, `05_missing_number_bt.py`, `05_missing_number_op1.py`, `05_missing_number_op2.py`

- 🚶 Brute Force:
  - For every number from 0 to n, check if it exists.
  - ❌ O(n²) — not scalable.

- 🔁 Better:
  - Use set/hashmap to check presence.
  - ✅ Fast lookup, O(n) space.

- ⚡ Optimal 1 (Sum):
  - Use sum formula and subtract actual sum.
  - ✅ O(n) time, O(1) space.

- ⚡ Optimal 2 (XOR):
  - XOR all elements with indices to find the missing one.
  - ✅ Very space efficient.

---

### 06. Remove Element

- 🔢 Files: `06_remove_element_bf.py`, `06_remove_element_bt.py`, `06_remove_element_op.py`

- 🚶 Brute Force:
  - Use new array to store values except target.
  - ✅ Clear logic, but uses space.

- 🔁 Better:
  - Manually shift elements left if match found.
  - ✅ More manual control, O(n) time.

- ⚡ Optimal:
  - Two-pointer approach from front.
  - ✅ Fast and in-place.

---

### 07. Squares of a Sorted Array

- 🔢 Files: `07_square_sorted_arr_bf.py`, `07_square_sorted_arr_op.py`

- 🚶 Brute Force:
  - Square all, sort the result.
  - ✅ Works fine, but not optimal.

- ⚡ Optimal:
  - Two-pointer from both ends since largest square can be at the end.
  - ✅ O(n) time without sorting.

---

### 08. Third Maximum Number

- 🔢 Files: `08_third_max_no_bf.py`, `08_third_max_no_bt.py`, `08_third_max_no_op.py`

- 🚶 Brute Force:
  - Sort and pick third distinct from end.
  - ✅ Simple but not efficient.

- 🔁 Better:
  - Use set + sort only distinct values.
  - ✅ Avoids duplicates.

- ⚡ Optimal:
  - Track top 3 max values manually in one pass.
  - ✅ Best performance and control.

---

### 09. Max Consecutive Ones

- 🔢 Files: `09_max_consecutives_bf.py`, `09_max_consecutives_op.py`

- 🚶 Brute Force:
  - Use loop and count each segment.
  - ✅ Easy logic, readable.

- ⚡ Optimal:
  - Single pass using counter with max.
  - ✅ O(n) time, cleaner and faster.

---

### 10. Single Number

- 🔢 Files: `10_single_number_bf.py`, `10_single_number_bt.py`, `10_single_number_op.py`

- 🚶 Brute Force:
  - Nested loop to count frequency.
  - ❌ O(n²) — inefficient.

- 🔁 Better:
  - Use hashmap to count frequency.
  - ✅ O(n) time, O(n) space.

- ⚡ Optimal:
  - XOR all numbers — duplicates cancel out.
  - ✅ Super efficient and elegant.

---

### 11. Two Sum

- 🔢 Files: `11_two_sum_bf.py`, `11_two_sum_op.py`

- 🚶 Brute Force:
  - Check every pair.
  - ❌ O(n²) — works for small input only.

- ⚡ Optimal:
  - Hashmap to store (target - current).
  - ✅ O(n) — most asked interview pattern.

---

### 12. Sort Colors

- 🔢 Files: `12_sort_colors_bf.py`, `12_sort_colors_op.py`

- 🚶 Brute Force:
  - Count 0s, 1s, 2s and overwrite.
  - ✅ Easy to understand.

- ⚡ Optimal:
  - Dutch National Flag Algorithm — 3 pointers.
  - ✅ O(n), in-place and no extra space.

---

### 13. Majority Element

- 🔢 Files: `13_majority_element_bf.py`, `13_majority_element_bt.py`, `13_majority_element_op.py`

- 🚶 Brute Force:
  - Count frequency of each element using nested loops.
  - ✅ Easy but inefficient (O(n²)).

- ⚙️ Better:
  - Use a HashMap (dictionary) to track frequencies.
  - ✅ O(n) time, O(n) space.

- ⚡ Optimal:
  - Moore’s Voting Algorithm to cancel out non-majority elements.
  - ✅ O(n) time, O(1) space, most efficient.

---

### 14. Palindrome Number

- 🔢 Files: `14_check_palindrome_no_bf.py`, `14_check_palindrome_no_bt.py`, `14_check_palindrome_no_op.py`

- 🚶 Brute Force:
  - Convert integer to string and compare with its reverse.
  - ✅ Simple and readable.

- ⚙️ Better:
  - Manually reverse the string without slicing.
  - ✅ Good for understanding string operations.

- ⚡ Optimal:
  - Reverse half the number mathematically.
  - ✅ O(log₁₀n) time, O(1) space, no string conversion.

---

### 15. Maximum Subarray

- 🔢 Files: `15_maximum_subarray_bf.py`, `15_maximum_subarray_bt.py`, `15_maximum_subarray_op.py`

- 🚶 Brute Force:
  - Try every subarray and calculate sum.
  - ✅ Easy to implement but O(n²) time.

- ⚙️ Better:
  - Use prefix sum array to compute subarray sums.
  - ✅ Slightly improved, still O(n²) time.

- ⚡ Optimal:
  - Kadane’s Algorithm tracks max sum while traversing.
  - ✅ O(n) time, O(1) space, most efficient.

---
### 16. Largest Element

- 🔢 Files:
  - `16_largest_element_bf.py`
  - `16_largest_element_bt.py`
  - `16_largest_element_op.py`

- 🚶 Brute Force:
  - For each element, check if any element is greater than it.
  - ✅ Simple to understand but runs in O(n²) time.

- ⚙️ Better:
  - Use Python’s built-in `max()` function to get the largest element.
  - ✅ More readable, still O(n) time, uses internal loop.

- ⚡ Optimal:
  - Traverse the array once while keeping track of the maximum value.
  - ✅ O(n) time and O(1) space — most efficient and cleanest approach.

---
### 17. Union of Two Sorted Arrays

* 🔢 Files:

  * `17_union_sorted_bf.py`
  * `17_union_sorted_bt.py`
  * `17_union_sorted_op.py`

* 🚶 Brute Force:

  * Combine both arrays, convert to set for uniqueness, and sort.
  * ✅ Simple and works, but involves sorting after set conversion.
  * ⏱ Time: O((n + m) log(n + m))

* ⚙️ Better:

  * Use two pointers and a `set` to collect unique elements during traversal.
  * ✅ Utilizes the sorted property, avoids unnecessary comparisons.
  * ⏱ Time: O(n + m), Space: O(n + m)

* ⚡ Optimal:

  * Use two pointers and directly build a result list, skipping duplicates manually.
  * ✅ Most efficient in terms of time and space (no extra structures like set).
  * ⏱ Time: O(n + m), Space: O(1) excluding output

---

### 18. Best Time to Buy and Sell Stock

* 🔢 Files:

  * `18_best_stock_bf.py`
  * `18_best_stock_bt.py`
  * `18_best_stock_op.py`

* 🚶 Brute Force:

  * Check all pairs `(buy_day, sell_day)` and track maximum profit.
  * ✅ Easy to implement but slow for large inputs.
  * ⏱ Time: O(n²)

* ⚙️ Better:

  * Use a prefix-min array to track the minimum price so far at each index.
  * ✅ Reduces time to linear, but adds O(n) space.
  * ⏱ Time: O(n), Space: O(n)

* ⚡ Optimal:

  * Single pass with two variables: `min_price_so_far` and `max_profit`.
  * ✅ O(n) time and O(1) space — the best way to solve this problem.
  * ⏱ Time: O(n), Space: O(1)

---

### 19. Leaders in an Array

* 🔢 Files:

  * `19_leaders_bf.py`
  * `19_leaders_op.py`

* 🚶 Brute Force:

  * For each element, check all elements to the right to see if it's a leader.
  * ✅ Simple logic but very inefficient.
  * ⏱ Time: O(n²)

* ⚡ Optimal:

  * Traverse from right to left, tracking `max_so_far` to identify leaders.
  * ✅ Most efficient and intuitive once understood.
  * ⏱ Time: O(n), Space: O(k) to store leaders, or O(1) if printed


---
20. Rearrange Array with Alternate Signs

🔢 Files:

20_rearrange_alternate_bf.py

20_rearrange_alternate_bt.py

🚶 Brute Force:

Traverse the array, store positives and negatives in separate lists.

Then merge them alternately into a result list.

✅ Easy to understand, preserves order.

⏱ Time: O(n), Space: O(n + n)

⚙️ Better:

Use two index pointers and directly place values into the result list at correct even/odd positions.

✅ No need for two separate lists, cleaner implementation.

⏱ Time: O(n), Space: O(n)

⚡ Optimal:

In-place rearrangement is not valid here due to order preservation requirement.

✅ So the better approach is also the optimal one in this case.
---

21. Next Permutation

🔢 Files:

21_next_permutation_bf.py

21_next_permutation_op.py

🚶 Brute Force:

Generate all permutations, sort them, and return the next one.

❌ Inefficient for large arrays.

⏱ Time: O(n! × n log n), Space: O(n!)

⚡ Optimal:

Traverse from right to left to find the first decreasing element.

Find the next greater element to swap and reverse the suffix.

✅ Time: O(n), Space: O(1), done in-place.

Follows the same logic as C++ STL’s std::next_permutation().
---
22. Longest Consecutive Sequence

🔢 Files:

22_longest_consecutive_bf.py

22_longest_consecutive_bt.py

22_longest_consecutive_op.py

🚶 Brute Force:

For each number, check if it starts a consecutive sequence.

Use a nested loop to track the sequence length.

❌ Inefficient for large inputs.

⏱ Time: O(n²), Space: O(1)

⚙️ Better:

Sort the array and count consecutive streaks.

Avoids duplicates and handles edge cases cleanly.

⏱ Time: O(n log n), Space: O(1) or O(n) depending on sort implementation

⚡ Optimal:

Use a HashSet for O(1) lookups.

Start counting only when current number is the start of a sequence.

✅ Best approach in terms of time and space.

⏱ Time: O(n), Space: O(n)

📌 Applications

Real-Life Applications:

Activity Tracking:

Find the longest streak of continuous activity (like steps, coding days, login streaks).

Database Record Analysis:

Detect consecutive record days with valid entries, sales, or production data.

Gaming Achievement Systems:

Unlock rewards based on longest consecutive wins, plays, or achievements.

IoT Device Monitoring:

Identify uninterrupted sensor activity or signal over consecutive time intervals.

Financial Analysis:

Analyze consecutive trading days with gains/losses for investment pattern recognition.

Algorithmic Concepts Practiced:

Hashing for O(1) lookup

Sequence identification and tracking

Set operations and search optimization


---



## 🧭 How to Use This Repo

1. Pick a problem.
2. Start with the `bf.py` to understand the brute-force logic.
3. Move to better/optimal solutions.
4. Practice on [LeetCode](https://leetcode.com/).

---

## ⭐ Tip for Beginners

> Always try brute force first. Optimization becomes easier when you understand the base logic.

---

## 👨‍💻 Suitable For

- Beginners learning DSA
- College students preparing for interviews
- Anyone seeking structured revision

---

## 🛠️ Tech Used

- Python 3.x
- VS Code + GitHub
- LeetCode problems

---

## 🔖 Upcoming Topics

- Hashing  
- Sliding Window  
- Two Pointers  
- Recursion  
- Linked List  
- Stack/Queue  

---

Happy Coding! 💻✨
