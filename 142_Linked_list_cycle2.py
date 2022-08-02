from sys import ps1
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
#Time:O(N)
#Space:O(N)


###### Floyd's solution:
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        slow = head
        fast = head
        while True:
            slow = slow.next
            fast = fast.next
            if fast == None or fast.next == None:
                return None
            else:
                fast = fast.next
            if fast == slow:
                break
        
        p1 = head
        p2 = fast
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1 

#Time:O(N)
#Space:O(1)