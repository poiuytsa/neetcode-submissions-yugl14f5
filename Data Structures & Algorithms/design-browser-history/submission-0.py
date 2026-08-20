class Node:
    def __init__(self,val,prev,next):
        self.val=val
        self.prev=prev 
        self.next=next 

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr=Node(homepage,None,None)
    
    #create node
    def visit(self, url: str) -> None:
        newNode=Node(url,self.curr,None)
        self.curr.next=newNode
        self.curr=self.curr.next

    def back(self, steps: int) -> str:
        i=0
        while i!=steps and self.curr.prev:
            self.curr=self.curr.prev
            i+=1
        return self.curr.val

    def forward(self, steps: int) -> str:
        i=0
        while i!=steps and self.curr.next:
            self.curr=self.curr.next 
            i+=1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)