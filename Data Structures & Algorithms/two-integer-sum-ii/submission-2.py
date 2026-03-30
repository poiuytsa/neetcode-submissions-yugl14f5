class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #O(n^2) time 
        #O(1) space 
        '''
        for i in range(len(numbers)-1):
            needed=target-numbers[i]
            for j in range(len(numbers)):
                if needed==numbers[j]:
                    return [i+1,j+1]
        '''

        l=0
        r=len(numbers)-1
        while True:
            if numbers[l]+numbers[r]==target:
                return[l+1,r+1]
            if numbers[l]+numbers[r]>target:
                r=r-1 
            else:
                l=l+1