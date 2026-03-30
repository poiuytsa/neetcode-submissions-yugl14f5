class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        visited=[]      #array that stores visited indices 

        for i,n in enumerate(strs):
            if i not in visited:
                bucket=[n]
                visited.append(i)
                for j in range(i+1,len(strs)):
                    #is anagram
                    if j not in visited:
                        if Counter(strs[i]) == Counter(strs[j]):
                            bucket.append(strs[j])
                            visited.append(j)
                res.append(bucket)
                bucket=[]
        
        return res 
