class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1 for j in range(m+1)]for i in range(n+1)]

        #base case
        for i in range(n+1):
            dp[i][0]=0

        for j in range(m+1):
            dp[0][j] = 0

        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if word1[ind1-1]==word2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = max(dp[ind1-1][ind2] , dp[ind1][ind2-1])

        lcs = dp[n][m]

        return n+m-(2*lcs)
        