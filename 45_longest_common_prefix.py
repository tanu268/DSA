"""
Problem 45 - Longest Common Prefix

🔹 Given a list of strings, return the longest common prefix among them.
🔹 Return "" if there is no common prefix.
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""

    # ✅ Take the first string as reference
    prefix = strs[0]

    # 🔁 Compare prefix with all other strings
    for word in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
        prefix = prefix[:i]  # trim prefix to matched portion

        # ⛔ Early stop if no common prefix
        if prefix == "":
            break

    return prefix

"""
🔸 Time Complexity: O(n * m), where
    n = number of strings
    m = length of the shortest string
🔸 Space Complexity: O(1) - no extra space (ignores output)
"""

# ---------------------------
# 🔁 Example Use Cases
# ---------------------------
if __name__ == "__main__":
    strs1 = ["flower", "flow", "flight"]
    print("Longest Common Prefix:", longestCommonPrefix(strs1))  # Output: "fl"

    strs2 = ["dog", "racecar", "car"]
    print("Longest Common Prefix:", longestCommonPrefix(strs2))  # Output: ""

    strs3 = ["interspecies", "interstellar", "interstate"]
    print("Longest Common Prefix:", longestCommonPrefix(strs3))  # Output: "inters"
