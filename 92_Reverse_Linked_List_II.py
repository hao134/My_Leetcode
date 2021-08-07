# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        m_prev = self.findkth(dummy, m - 1)
        m = m_prev.next
        n = self.findkth(dummy, n)
        n_next = n.next
        n.next = None

        self.reverse(m)
        m_prev.next = n
        m.next = n_next

        return dummy.next

    # Linked list 反轉，要記一下
    def reverse(self, head):
        prev = None
        while head != None:
            next_head = head.next
            head.next = prev
            prev = head
            head = next_head

    def findkth(self, head, k):
        for i in range(k):
            if head is None:
                return None
            head = head.next
        return head

# Solution 2 -> Stack
class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 1. 查看 m 是否等於n
        if m == n: return head
        # 2. define a iterate node and walk through to place m - 1 to find the left node
        st = []
        left, node = None, head
        if m != 1:
            for i in range(1, m - 1):
                node = node.next
            left = node
            node = node.next # now node at position m
        # 3. walk through every node from m to n and put every node to stack st

        for i in range(m, n + 1):
            st.append(node)
            node = node.next

        # After the loop, the node at position n + 1

        # 4. Take out the nodes in Stack in turn, and connect the next of all nodes in sequence,
        # Until there are no more nodes in the Stack.
        l1, l2 = st.pop(), None
        if m ==1:
            head = l1
        else:
            left.next = l1
        while st:
            l2 = st.pop()
            l1.next = l2
            l1 = l2

        l1.next = node
        return head

# 我覺的方法一比較好記，方法二參考一下