class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=0
        i=0
        while i<len(nums)-res:
            if nums[i]==val:
                nums[i],nums[len(nums)-1-res]=nums[len(nums)-1-res],nums[i]
                res+=1
            else:
                i+=1
        print(res)
        print(nums)
        return len(nums)-res