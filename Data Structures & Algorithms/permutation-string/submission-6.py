class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r=len(s1)-1
        for i in range(len(s2)-len(s1)+1):
                print(s2[i:r+1])
                if Counter(s1)==Counter(s2[i:r+1]):
                        return True 
                r+=1
        return False 