
# Definition for a Node.
#TODO UNFINISHED 
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup : {int:Node}= dict()

        newHead = Node()

    def copyNode(self, ogNode, newNode):
        newNode.val = ogNode.val
        newNode.next

        