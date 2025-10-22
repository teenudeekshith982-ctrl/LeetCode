class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        sum = 0
        for i in range(k):
            sum+=cardPoints[i]
        
        l = k-1
        r = n-1
        ans = sum
        while(l>=0):
            sum-=cardPoints[l]
            sum+=cardPoints[r]
            ans = max(ans,sum)
            l-=1
            r-=1
        return ans

        


        