# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # tempSum=l1.val+l2.val
        # if tempSum<=9:
        #     head=Node(tempSum)
        # else:
        #     head=Node(tempSum%10)
        #     head.next(1)

        isCarry=False
        curr=ListNode(0)
        head=curr
        prev=None
        while l1 and l2:
            tempSum=l1.val+l2.val+isCarry
            if tempSum<=9:
                curr.val=tempSum
                isCarry=False
            else:
                curr.val=tempSum%10
                isCarry=True

            l1=l1.next
            l2=l2.next
            prev=curr
            newNode=ListNode(0)
            curr.next=newNode
            curr=newNode
            

        if not l1 and not l2:
            if curr.val==0:
                prev.next=None

            if isCarry:
                lastNode=ListNode(1,None)
                prev.next=lastNode
        
        if l1 and not l2:
            while l1:
                tempSum=l1.val+isCarry
                if tempSum<=9:
                    curr.val=tempSum
                    isCarry=False
                else:
                    curr.val=tempSum%10
                    isCarry=True 
                l1=l1.next
                prev=curr
                newNode=ListNode(0)
                curr.next=newNode
                curr=newNode

        if not l1 and l2:
            while l2:
                tempSum=l2.val+isCarry
                if tempSum<=9:
                    curr.val=tempSum
                    isCarry=False
                else:
                    curr.val=tempSum%10
                    isCarry=True 
                l2=l2.next
                prev=curr
                newNode=ListNode(0)
                curr.next=newNode
                curr=newNode

        if curr.val==0:
            prev.next=None

        if isCarry:
            lastNode=ListNode(1,None)
            prev.next=lastNode


        return head