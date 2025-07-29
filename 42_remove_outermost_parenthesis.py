"""
Problem 42 - Remove Outermost Parentheses

🔹 Given a valid parentheses string, remove the outermost pair of parentheses from every primitive component.
"""

def removeOuterParentheses(s):
    result = []
    count = 0  # stack depth

    for ch in s:
        if ch == '(':
            if count > 0:
                result.append(ch)  # not the outermost '('
            count += 1
        else:  # ch == ')'
            count -= 1
            if count > 0:
                result.append(ch)  # not the outermost ')'

    return ''.join(result)

"""
🔸 Time Complexity: O(n) - single pass over the string
🔸 Space Complexity: O(n) - for storing result (output only)
"""

# ---------------------------
# 🔁 Example Use Cases
# ---------------------------
if __name__ == "__main__":
    s1 = "(()())(())"
    print("After removing outermost:", removeOuterParentheses(s1))  # Output: "()()()"

    s2 = "(()())(())(()(()))"
    print("After removing outermost:", removeOuterParentheses(s2))  # Output: "()()()()(())"

    s3 = "()()"
    print("After removing outermost:", removeOuterParentheses(s3))  # Output: ""
