"""
🔹 Problem 242 - Valid Anagram

🔸 Description:
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An anagram is a word formed by rearranging the letters of a different word, using **all the original letters exactly once**.

Example:
Input: s = "anagram", t = "nagaram"
Output: True

🔸 Constraints:
- 1 <= s.length, t.length <= 5 * 10⁴
- s and t consist of lowercase English letters
"""

def isAnagram(s: str, t: str) -> bool:
    """
    Checks if string t is an anagram of string s using character count comparison.
    """
    # ✅ Quick fail if lengths don't match
    if len(s) != len(t):
        return False

    # ✅ Use a dictionary to count letters in s
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    # ✅ Subtract counts using letters in t
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


# 🔹 Example Use Case
if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))  # Expected: True
    print(isAnagram("rat", "car"))          # Expected: False
