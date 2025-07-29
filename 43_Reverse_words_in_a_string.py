"""
Problem 43 - Reverse Words in a String

🔹 Given a string, reverse the words.
🔹 Remove extra spaces and keep only one space between words.
"""

def reverseWords(s):
    # 🔽 Step 1: Split the string into words using split()
    words = s.split()

    # 🔁 Step 2: Reverse the list of words
    words.reverse()

    # 🔗 Step 3: Join the reversed words with a single space
    return ' '.join(words)

"""
🔸 Time Complexity: O(n) - one pass to split, one to reverse, one to join
🔸 Space Complexity: O(n) - uses a list to hold words
"""

# ---------------------------
# 🔁 Example Use Cases
# ---------------------------
if __name__ == "__main__":
    s1 = "  hello   world  "
    print("Reversed:", reverseWords(s1))  # Output: "world hello"

    s2 = "a good   example"
    print("Reversed:", reverseWords(s2))  # Output: "example good a"

    s3 = "  sky   is  blue "
    print("Reversed:", reverseWords(s3))  # Output: "blue is sky"
