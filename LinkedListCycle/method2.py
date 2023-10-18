'''
Floyd's Cycle Detection Algorithm
'''

#Please Copilot let me do this on my own. 

class Node:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = next

class Solution:
    def hasCycle(self, head: Node):

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
print(Solution.hasCycle(Solution, Node(1, Node(2, Node(3, Node(4, Node(5)))))))