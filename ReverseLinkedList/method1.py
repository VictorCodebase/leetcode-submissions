
# 0(1) implementation

class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

class Solution:
     def reverseList(self, head: ListNode) -> ListNode:
          prev, curr = None, head

          while curr:
              nxt  = curr.next
              curr.next = prev
              prev = curr
              curr = nxt
          return prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
reversed_head = solution.reverseList(head)
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next

