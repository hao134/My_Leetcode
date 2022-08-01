from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        currentNode = head
        while currentNode:
            if currentNode.child == None:
                currentNode = currentNode.next
            else:
                tail = currentNode.child
                # why tail.next? we want the node stop at the the final node, not the final node's next node
                # at first while, we don't use currentNode.next, because we want the node stop
                # at the final's next -> None
                while tail.next:
                    tail = tail.next
                    tail.next = currentNode.next
                    if tail.next != None:
                        tail.next.prev = tail

                currentNode.next = currentNode.child
                currentNode.next.prev = currentNode
                currentNode.child = None
        return head
