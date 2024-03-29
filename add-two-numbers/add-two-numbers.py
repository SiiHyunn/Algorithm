class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resultNode = tempNode = ListNode()
        
        tmp = 0
        
        while l1 or l2 or tmp:
            l1_val = 0
            l2_val = 0
            
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            
            result = l1_val + l2_val + tmp
            
            new_val = result % 10
            tmp = result // 10
            tempNode.next = ListNode(new_val)
            tempNode = tempNode.next
            
        return resultNode.next
        