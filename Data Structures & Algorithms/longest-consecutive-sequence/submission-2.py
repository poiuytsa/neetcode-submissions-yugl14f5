class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        maxlen=0

        if not len(nums):
            return 0 

        for n in seen:
            if n-1 not in seen:
                a=n+1 
                currlen=0
                while a in seen:
                    currlen+=1 
                    a+=1
                maxlen=max(currlen,maxlen)
        return maxlen+1
