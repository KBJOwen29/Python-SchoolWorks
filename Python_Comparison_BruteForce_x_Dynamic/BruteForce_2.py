def trap_brute(height: list[int]) -> int:
    n = len(height)
    res = 0

    for i in range(n):
        # Find max height to the left of current index
        left_max = max(height[:i+1])
        # Find max height to the right of current index
        right_max = max(height[i:])

        # Water trapped = min(left, right) - height at current index
        res += min(left_max, right_max) - height[i]

    return res
