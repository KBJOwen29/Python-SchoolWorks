def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP table where dp[i][w] represents the maximum value for the first i items and capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Include the item or exclude it - take max value
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Cannot include the item, keep previous max
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity], dp

# Example usage
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    max_value, dp_table = knapsack(weights, values, capacity)
    print("Maximum value in knapsack:", max_value)

    # (Optional) Display the DP table
    print("\nDP Table:")
    for row in dp_table:
        print(row)
