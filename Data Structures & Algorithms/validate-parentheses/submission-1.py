class Solution:
    def isValid(self, s: str) -> bool:
        opened='([{'
        closed=')}]'
        stack=[]
        for n in s:     
                if n in opened:
                        stack.append(n)
                if n in closed:
                        if len(stack)==0:
                                return False
                        x = stack.pop()
                        if (x=="(" and n==')') or (x=="{" and n=='}') or (x=="[" and n==']'):
                                continue 
                        else:
                                return False 
        
        if len(stack)==0:
                return True 
        return False  