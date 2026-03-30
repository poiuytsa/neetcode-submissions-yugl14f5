class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for n in strs:
            res+=str(len(n))+"#"+n
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0 
        while i<len(s):
            length=""
            if s[i].isdigit():
                while s[i].isdigit() and i<len(s):
                    length+=s[i]
                    i+=1 
            curr=""
            length=int(length)
            if s[i]=="#":
                i+=1 
                while length>0 and i<len(s):
                    curr+=s[i]
                    length-=1
                    i+=1 
            res.append(curr)
            
        return res