class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for word in words:
            for w2 in words:
                if word in w2 and word!=w2:
                    res.append(word)
                    break
        return res