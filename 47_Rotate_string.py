"""
🔹 Problem 796 - Rotate String

🔸 Description:
Given two strings `s` and `goal`, return `True` if and only if `s` can become `goal` after some number of **rotations**.
A rotation is moving the first character of `s` to the end.

Example:
Input: s = "abcde", goal = "cdeab"
Output: True

Explanation:
- Rotate "abcde" once → "bcdea"
- Rotate again → "cdeab" ✅ matches goal

🔸 Constraints:
- 1 <= s.length, goal.length <= 100
- s and goal consist of lowercase English letters
"""

def rotateString(s: str, goal: str) -> bool:
    """
    Checks if goal can be obtained by rotating string s any number of times.
    """
    # If lengths differ, rotation is impossible
    if len(s) != len(goal):
        return False

    # Check if goal is a substring of s+s (all possible rotations)
    return goal in (s + s)


# 🔹 Example Use Case
if __name__ == "__main__":
    print(rotateString("abcde", "cdeab"))  # Expected: True
    print(rotateString("abcde", "abced"))  # Expected: False
