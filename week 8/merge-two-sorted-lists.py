# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        merged = head
        if list1 == None: return list2
        if list2 == None: return list1
        
        while list1 != None and list2 != None:
            
                
            if list1.val < list2.val:
                head.val = list1.val
                list1 = list1.next
            else:
                head.val = list2.val
                list2 = list2.next  
        
            if list1 == None:
                head.next = list2
                break
            elif list2 == None:
                head.next = list1
                break
            
            
            head.next = ListNode()
            head = head.next
            

                
        return merged
                
                
