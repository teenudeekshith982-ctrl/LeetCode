class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        sum = 0
        for i in nums:
            if(i==0):
                sum=0
            else:
                sum+=i
                count = max(sum,count)

        return count