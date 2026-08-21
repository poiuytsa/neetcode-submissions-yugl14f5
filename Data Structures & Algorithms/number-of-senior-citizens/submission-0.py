class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res=0
        for n in details:
            #0-9 -> phone no
            #10 -> gender
            #11-12 -> age
            if int(n[11:13])>60:
                res+=1 
        return res 