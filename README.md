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
