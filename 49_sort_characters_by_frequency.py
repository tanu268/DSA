"""
🔹 Problem 451 - Sort Characters By Frequency

🔸 Description:
Given a string `s`, return a string sorted in **decreasing order** based on the frequency of the characters.
Characters with higher frequency should appear earlier. If multiple characters have the same frequency, their relative order can be arbitrary.

Example:
Input: s = "tree"
Output: "eert"  # 'e' appears twice so comes first

🔸 Constraints:
- 1 <= s.length <= 5 * 10⁵
- s consists of ASCII characters.
"""

from collections import Counter

def frequencySort(s: str) -> str:
    """
    Sorts characters in s by descending frequency using a frequency map and sorting.
    """
    # Count frequency of each character
    freq = Counter(s)

    # Sort characters by frequency descending and build the result
    # Each character `char` is repeated `count` times
    sorted_chars = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return "".join(char * count for char, count in sorted_chars)


# 🔹 Example Use Case
if __name__ == "__main__":
    print(frequencySort("tree"))      # Expected: "eert" or "eetr"
    print(frequencySort("cccaaa"))    # Expected: "cccaaa" or "aaaccc"
    print(frequencySort("Aabb"))      # Expected: "bbAa" or "bbaA"
