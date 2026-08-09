class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        res=set()

        for n in triplets:

            #not possible 
            if n[0]>target[0] or n[1]>target[1] or n[2]>target[2]:
                continue 
            
            for i in range(3):
                if n[i]==target[i]:
                    res.add(i)
                
        return len(res)==3
