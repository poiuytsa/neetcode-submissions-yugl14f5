class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len=0
        max_l=0
        max_r=0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                # print(s[i:j+1])
                # print(s[j:i-1:-1])
                if i==0:
                    if s[i:j+1]==s[j::-1]:
                        if max_len<j-i+1:
                            max_len=j-i+1
                            max_l=i
                            max_r=j
                else:
                    if s[i:j+1]==s[j:i-1:-1]:
                        if max_len<j-i+1:
                            max_len=j-i+1
                            max_l=i
                            max_r=j
        return s[max_l:max_r+1]
