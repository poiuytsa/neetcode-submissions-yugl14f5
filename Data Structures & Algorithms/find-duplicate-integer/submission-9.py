class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return nums[i]


        # numSet=set()
        # for n in nums:
        #     if n in numSet:
        #         return n
        #     numSet.add(n) 

        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
            
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow 