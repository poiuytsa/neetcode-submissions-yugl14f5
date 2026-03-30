class Solution:
    def isPalindrome(self, s) :
        s1=''
        for c in s:
            if c.isalnum():
                s1+=c

        return s1.lower()==s1[::-1].lower()