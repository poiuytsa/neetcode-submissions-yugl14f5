class Solution:
    def longestPalindrome(self, s: str) -> str:

        #brute force

        # max_len=0
        # max_l=0
        # max_r=0
        # for i in range(len(s)-1):
        #     for j in range(i+1,len(s)):
        #         # print(s[i:j+1])
        #         # print(s[j:i-1:-1])
        #         if i==0:
        #             if s[i:j+1]==s[j::-1]:
        #                 if max_len<j-i+1:
        #                     max_len=j-i+1
        #                     max_l=i
        #                     max_r=j
        #         else:
        #             if s[i:j+1]==s[j:i-1:-1]:
        #                 if max_len<j-i+1:
        #                     max_len=j-i+1
        #                     max_l=i
        #                     max_r=j
        # return s[max_l:max_r+1]


        #center expansion
        max_l,max_r,max_len=0,0,0

        #odd length palindromes
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if max_len<r-l+1:
                    max_l=l
                    max_r=r
                    max_len=r-l+1
                l-=1
                r+=1


        #even length palindromes
        for i in range(len(s)):
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if max_len<r-l+1:
                    max_l=l
                    max_r=r
                    max_len=r-l+1
                l-=1
                r+=1


        return s[max_l:max_r+1]
