# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #2 pass solution 
        '''
        length=0
        curr=head 
        while curr:
            length+=1
            curr=curr.next 
        
        if n==length:
            return head.next

        i=0
        curr=head
        while i!=(length-n-1):
            curr=curr.next
            i+=1 
        
        curr.next=curr.next.next 

        return head 
        '''

        #1 pass solution 
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next