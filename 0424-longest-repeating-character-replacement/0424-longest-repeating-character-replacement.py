class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        hash = [0] * 26
        maxfreq = 0
        maxlen = 0
        while(r<n):

            hash[ord(s[r])-ord('A')]+=1

            maxfreq = max(maxfreq,hash[ord(s[r])-ord('A')])

            if((r-l+1)-maxfreq > k):
                hash[ord(s[l])-ord('A')]-=1
                l+=1

            maxlen = max(maxlen,r-l+1)
            r+=1

        return maxlen

        