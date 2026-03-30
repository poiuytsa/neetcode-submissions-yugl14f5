class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]

        if len(nums)==0:
            return []
        
        nums.sort()
        if nums[0]>0:
            return []
        
        for i in range(len(nums)-2):

            if i>=1 and nums[i]==nums[i-1]:
                continue

            need=-nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]==need:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1 
                    r-=1 
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]>need:
                    r-=1
                else:
                    l+=1 

        return res 
