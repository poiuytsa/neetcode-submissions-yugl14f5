class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # sum:number of times
        prefix_sum_count=defaultdict(int)
        prefix_sum_count[0]=1
        curr_sum,res=0,0
        for n in nums:  
            curr_sum+=n
            if curr_sum-k in prefix_sum_count:
                res+=prefix_sum_count[curr_sum-k]
            prefix_sum_count[curr_sum]+=1
        return res

