#Brute Force 1.

def isMatch_brute(s: str, p: str) -> bool:
    # Base case: if pattern is empty, return True only if string is also empty
    if not p:
        return not s

    # Check if the first character matches (considering '.' wildcard)
    first_match = bool(s) and (s[0] == p[0] or p[0] == '.')

    # If the next character in pattern is '*', we have two choices:
    # 1. Skip the '*' and its preceding char (zero occurrences)
    # 2. If first character matches, move ahead in string (consume one char)
    if len(p) >= 2 and p[1] == '*':
        return (isMatch_brute(s, p[2:]) or
                (first_match and isMatch_brute(s[1:], p)))
    else:
        # Move to the next character in both string and pattern
        return first_match and isMatch_brute(s[1:], p[1:])
