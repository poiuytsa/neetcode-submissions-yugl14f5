class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for n in tokens:
                if n=="+":
                        x=stack.pop()
                        y=stack.pop()
                        stack.append(int(x)+int(y))
                elif n=="-":
                        x=stack.pop()
                        y=stack.pop()
                        stack.append(int(y)-int(x))
                elif n=="*":
                        x=stack.pop()
                        y=stack.pop()
                        stack.append(int(x)*int(y))
                elif n=="/":
                        x=stack.pop()
                        y=stack.pop()
                        stack.append(int(y/x))
                else:
                        stack.append(int(n))
        return stack[0]