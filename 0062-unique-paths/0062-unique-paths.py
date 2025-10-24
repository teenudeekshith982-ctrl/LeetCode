class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for j in range(n)]for i in range(m)]
        
        dp[0][0]=1

        for i in range(m):
            for j in range(n):
                if(i==0 and j==0):
                    continue

                ans = 0
                if(i-1>=0):
                    ans+=dp[i-1][j]
                if(j-1>=0):
                    ans+=dp[i][j-1]

                dp[i][j]=ans
        return dp[m-1][n-1]
