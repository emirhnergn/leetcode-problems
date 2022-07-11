# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        temp_head = head
        temp_list = []
        while True:
            try:
                temp_list.append(temp_head.val)
                temp_head = temp_head.next
                i += 1
            except:
                break
        if i == 1:
            return head.next
        temp_list.pop(len(temp_list)-n)
        for k in range(len(temp_list)-1,-1,-1):
            if k == len(temp_list)-1:
                listnode = ListNode(temp_list[k])
            else:
                listnode = ListNode(temp_list[k],listnode)
        return listnode