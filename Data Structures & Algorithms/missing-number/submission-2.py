class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #return int(((len(nums)*(len(nums)+1))/2))-sum(nums)

        res=0
        for i in range(len(nums)+1):
            res=res^i
        for n in nums:
            res=res^n
        return res