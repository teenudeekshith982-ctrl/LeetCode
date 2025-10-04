class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        r_maxi = arr[n-1]
        ans = [0]*n
        ans[n-1]=-1

        for i in range(n-2,-1,-1):
            
            ans[i] = r_maxi
            r_maxi = max(r_maxi,arr[i])
        return ans