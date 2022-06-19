# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ite = head
        while ite:
            tmp = ite.next
            while tmp and ite.val == tmp.val:
                tmp = tmp.next
            ite.next = tmp
            ite = tmp
        return head