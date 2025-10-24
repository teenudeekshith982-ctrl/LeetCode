class Solution:
    def solve(self,i,j,m,n,dp):
        if(i==0 and j==0):
            return 1

        if dp[i][j]!=-1:
            return dp[i][j]

        ans = 0

        if(j-1>=0):
            ans+=self.solve(i,j-1,m,n,dp)
        if(i-1>=0):
            ans+=self.solve(i-1,j,m,n,dp)
        dp[i][j]=ans
        return ans
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for j in range(n)]for i in range(m)]
        return self.solve(m-1,n-1,m,n,dp)
        