class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        # If (target + total_sum) is odd or target is out of range, no solution
        if (target + total_sum) % 2 != 0 or total_sum < abs(target):
            return 0

        subset_sum = (target + total_sum) // 2

        n = len(nums)
        dp = [[0 for _ in range(subset_sum + 1)] for _ in range(n + 1)]

        # Base case: there's one way to make sum 0 — by taking nothing
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill DP table
        for i in range(1, n + 1):
            for s in range(0, subset_sum + 1):
                notTake = dp[i - 1][s]
                take = 0
                if nums[i - 1] <= s:
                    take = dp[i - 1][s - nums[i - 1]]
                dp[i][s] = take + notTake

        return dp[n][subset_sum]