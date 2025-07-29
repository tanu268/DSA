"""
Problem 46 - Isomorphic Strings

🔹 Check if two strings are isomorphic.
🔹 Characters in 's' must map uniquely to characters in 't'.
"""

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    # Two dictionaries to track mappings both ways
    map_s_t = {}
    map_t_s = {}

    for ch_s, ch_t in zip(s, t):
        # ✅ Check s -> t mapping
        if ch_s in map_s_t:
            if map_s_t[ch_s] != ch_t:
                return False
        else:
            map_s_t[ch_s] = ch_t

        # ✅ Check t -> s mapping
        if ch_t in map_t_s:
            if map_t_s[ch_t] != ch_s:
                return False
        else:
            map_t_s[ch_t] = ch_s

    return True

"""
🔸 Time Complexity: O(n), where n = length of the strings
🔸 Space Complexity: O(1), since there are only 256 ASCII characters
"""

# ---------------------------
# 🔁 Example Use Cases
# ---------------------------
if __name__ == "__main__":
    s1, t1 = "egg", "add"
    print(f"'{s1}' and '{t1}' are isomorphic:", isIsomorphic(s1, t1))  # Output: True

    s2, t2 = "foo", "bar"
    print(f"'{s2}' and '{t2}' are isomorphic:", isIsomorphic(s2, t2))  # Output: False

    s3, t3 = "paper", "title"
    print(f"'{s3}' and '{t3}' are isomorphic:", isIsomorphic(s3, t3))  # Output: True
