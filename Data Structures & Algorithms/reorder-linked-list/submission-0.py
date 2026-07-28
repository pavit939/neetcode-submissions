# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        #Middle Node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_begin = slow.next
        prev = slow.next = None
        #Reversing second half
        while second_begin:
            next_node = second_begin.next
            second_begin.next = prev
            prev = second_begin
            second_begin = next_node
        first, second = head, prev
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next



        
        