class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        #cheese
        # num=0
        # for n in digits:
        #     num=(num*10)+n
        # num+=1
        # res=[]
        # while num:
        #     res.append(num%10)
        #     num//=10
        # return res[::-1]

        
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0

        return [1]+digits