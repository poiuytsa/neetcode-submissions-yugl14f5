class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left():
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                m=(l+r)//2
                if nums[m]<target:
                    l=m+1
                else:
                    res=m
                    r=m-1
            return res if res!=-1 and nums[res]==target else -1 


        def right():
            l=0
            r=len(nums)-1
            res=-1 
            while l<=r:
                m=(l+r)//2
                if nums[m]<=target:
                    res=m
                    l=m+1
                else:
                    r=m-1
            return res if res!=-1 and nums[res]==target else -1

        return([left(),right()])