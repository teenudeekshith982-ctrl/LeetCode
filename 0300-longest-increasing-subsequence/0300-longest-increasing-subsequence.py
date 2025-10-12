class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[ 1 for i in range(n)]

        for ind in range(1,n):
            for prev_ind in range(ind):
                if(nums[prev_ind]<nums[ind]):
                    dp[ind] = max(dp[ind] , 1+dp[prev_ind] )

        return max(dp)
        