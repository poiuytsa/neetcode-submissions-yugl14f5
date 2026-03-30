class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}   #value:freq 
        for n in nums:
            freq[n] = freq.get(n,0)+1
        
        for k,v in freq.items():
            if v>=2:
                return True
        
        return False