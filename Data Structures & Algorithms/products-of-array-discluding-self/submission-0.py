class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPro=[]
        suffixPro=[0]*len(nums)

        temp=1 
        for n in nums:
            temp*=n
            prefixPro.append(temp)
        
        temp=1
        for i in range(len(nums)-1,-1,-1):
            temp*=nums[i]
            suffixPro[i]=temp
        
        res=[]
        for i in range(len(nums)):
            if i==0:
                res.append(suffixPro[1])
            elif i==len(nums)-1:
                res.append(prefixPro[-2])
            else:
                res.append(prefixPro[i-1]*suffixPro[i+1])
        
        return res