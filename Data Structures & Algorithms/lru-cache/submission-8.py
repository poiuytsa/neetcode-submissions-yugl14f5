class Node:
    def __init__(self,key,value,prev,next):
        self.key=key
        self.value=value 
        self.prev=prev 
        self.next=next

#LRU------->MRU
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity 
        self.cache={}
        self.head=Node(-1,-1,None,None)
        self.tail=Node(-1,-1,None,None)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]

            #moving it to right most 
            node.next.prev=node.prev 
            node.prev.next=node.next

            self.tail.prev.next=node
            node.prev=self.tail.prev
            node.next=self.tail
            self.tail.prev=node 

            return node.value
        return -1

    def put(self, key: int, value: int) -> None:

        #if key already exists, update
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            node.next.prev=node.prev
            node.prev.next=node.next
            self.tail.prev.next=node
            node.prev=self.tail.prev
            node.next=self.tail
            self.tail.prev=node
            return


        if len(self.cache)<self.capacity:
            node=Node(key,value,self.tail.prev,self.tail)
            self.tail.prev.next=node
            self.tail.prev=node
            self.cache[key]=node

        else:
            delete=self.head.next
            self.head.next=delete.next
            delete.next.prev=self.head
            del self.cache[delete.key]

            node=Node(key,value,self.tail.prev,self.tail)
            self.tail.prev.next=node
            self.tail.prev=node
            self.cache[key]=node

