class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        sum = 0
        maxi = float('-inf')
        for i in range(n):
            sum+=nums[i]

            maxi = max(sum,maxi)

            if(sum<0):
                sum = 0

        return maxi
        