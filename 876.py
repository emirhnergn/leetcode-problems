# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        temp_head = head
        while True:
            try:
                temp_head = temp_head.next
                i += 1
            except:
                break
        tmp = []
        if i == 1:
            return head
        elif i % 2 == 0:
            for k in range(i//2):
                try:
                    tmp = tmp.next
                except:
                    tmp = head.next
            return tmp
        else:
            for k in range(i//2):
                try:
                    tmp = tmp.next
                except:
                    tmp = head.next
            return tmp