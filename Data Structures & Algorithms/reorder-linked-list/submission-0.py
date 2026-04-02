# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #finding midpoint 
        mid,fast=head,head
        while fast and fast.next:
            mid=mid.next 
            fast=fast.next.next 
        
        #detaching the halves 
        curr=head
        while curr.next is not mid:
            curr=curr.next 
        curr.next=None

        #reversing the latter half 
        prev,curr=None,mid 
        while curr:
            temp=curr.next 
            curr.next=prev 
            prev=curr 
            curr=temp
        mid=prev 

        #merge 
        newHead=head 
        head=head.next
        curr=newHead
        while head and mid:
            curr.next=mid
            mid=mid.next
            curr.next=head 
            curr=curr.next
        if head:
            curr.next=head
        if mid:
            curr.next=mid 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
