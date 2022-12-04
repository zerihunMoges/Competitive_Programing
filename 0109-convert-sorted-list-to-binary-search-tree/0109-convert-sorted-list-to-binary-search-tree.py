# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def toBST(self, nums):
        if not nums:
            return None
        
        mid = nums[len(nums)//2]
        cur = TreeNode(mid)
        
        cur.left = self.toBST(nums[:len(nums)//2])
        cur.right = self.toBST(nums[len(nums)//2+1:])
        
        return cur
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        return self.toBST(nums)