class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        hash_map = {}
        max_len = 0

        while(r<n):

            if(s[r] in hash_map and hash_map[s[r]]>=l):
                l = hash_map[s[r]]+1
            
            max_len = max(max_len,r-l+1)
            hash_map[s[r]]=r
            
            r+=1

        return max_len
        
        