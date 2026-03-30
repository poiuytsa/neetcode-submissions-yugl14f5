class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        longest_ss=set()

        for r in range(len(s)):
            while s[r] in longest_ss:
                longest_ss.remove(s[l])
                l+=1
            longest_ss.add(s[r])
            res=max(res,r-l+1)

        return res