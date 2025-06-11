# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def makeStack(first):
            stack = []
            while first != None:
                stack.append(first)
                first = first.next
            return stack
            
        #find the middle
        slow = head; fast = head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        stack = makeStack(slow.next)

        while stack != []:
            temp = head.next
            head.next = stack.pop()
            head = head.next
            head.next = temp
            head = head.next

        head.next = None