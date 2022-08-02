from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}
        while head:
            if head not in seen:
                seen[head] = True
            else:
                return head
            head = head.next
        
        return None