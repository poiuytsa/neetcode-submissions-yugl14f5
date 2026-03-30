class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        visited=[]
        for i in range(len(strs)):
            currBucket=[]
            if i not in visited:
                currBucket.append(strs[i])
                for j in range(i+1,len(strs)):
                    if (Counter(strs[i])==Counter(strs[j])):
                        currBucket.append(strs[j])
                        visited.append(j)
                res.append(currBucket)
        return res
