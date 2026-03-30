class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(nlogn)
        #return sorted(s)==sorted(t)

        #O(n) 
        return Counter(s)==Counter(t)