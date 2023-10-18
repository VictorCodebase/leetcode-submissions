
class Node:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = next

class Solution:
    #On2 solution
    def hasCycle(self, head: Node):
        if head is None:
            return False
        list = []
        while head:
            if head in list:
                return True
            list.append(head)
            head = head.next
        return False

#print(Solution.hasCycle(Solution, Node(1, Node(2, Node(3, Node(4, Node(5)))))))
# Provide data input that has a cycle
print(Solution.hasCycle(Solution, Node(1, Node(2, Node(3, Node(4, Node(5)))))))

        
