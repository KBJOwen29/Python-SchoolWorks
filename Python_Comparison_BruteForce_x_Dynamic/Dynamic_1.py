def isMatch_dp(s: str, p: str) -> bool:
    memo = {}  # Store results of subproblems (i, j)

    def dp(i: int, j: int) -> bool:
        if (i, j) in memo:
            return memo[(i, j)]

        # If pattern is exhausted, check if string is also exhausted
        if j == len(p):
            ans = i == len(s)
        else:
            # Check if current characters match
            first = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # Handle '*' wildcard in pattern
            if (j + 1) < len(p) and p[j+1] == '*':
                # Two choices: skip or consume
                ans = dp(i, j+2) or (first and dp(i+1, j))
            else:
                ans = first and dp(i+1, j+1)

        memo[(i, j)] = ans  # Save result to avoid recomputation
        return ans

    return dp(0, 0)
