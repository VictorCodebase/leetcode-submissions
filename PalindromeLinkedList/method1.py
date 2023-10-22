
class Node:
    def __init__(self, data, next) -> None:
        data = data
        next = next

class Solution:
    def isPalindrome(self, head: Node) -> bool:
        
        characters = []
        while head:
            print(head)
            characters += head
            head = head.next

Solution.isPalindrome(Solution, Node(1, Node(2, Node(3, Node(4, Node(5))))))