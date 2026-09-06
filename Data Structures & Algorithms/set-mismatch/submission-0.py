class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # numSet = set(nums)
        # n = len(nums)
        # missing = -1

        # for i in range(1,n+1):
        #     if i not in numSet:
        #         missing = i
            
        
        # freq = Counter(nums)
        # print(freq)
        # for k,v in freq.items():
        #     if v == 2:
        #         return [k,missing]

        n = len(nums)
        real_sum = sum(nums)
        unique_sum = sum(set(nums))
        expected_sum = (n*(n+1))//2

        return [real_sum - unique_sum, expected_sum - unique_sum]