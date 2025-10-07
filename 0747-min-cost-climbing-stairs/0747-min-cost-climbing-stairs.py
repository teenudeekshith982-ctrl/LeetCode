class Solution:
    def f(self,ind,cost,dp):

        if(ind==0):
            return cost[0]

        if(ind==1):
            return cost[1]

        if dp[ind]!=-1:
            return dp[ind]

        ans = cost[ind] + min(self.f(ind-1,cost,dp) , self.f(ind-2,cost,dp))
        dp[ind] = ans
        return ans
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for i in range(n)]
        return min(self.f(n-1,cost,dp) , self.f(n-2,cost,dp))