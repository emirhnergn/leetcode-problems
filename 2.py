# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1String = ""
        list2String = ""
        while True:
            try:
                list1String = str(l1.val) + list1String
                l1 = l1.next
            except:
                break
        while True:
            try:
                list2String = str(l2.val) + list2String
                l2 = l2.next
            except:
                break
        def createListNode(string):
            if len(string) == 1:
                return ListNode(string)
            else:
                deneme = ListNode(val=int(string[-1]),next=(createListNode(string[:-1])))
                return deneme
        answer = str(int(list1String) + int(list2String))
        ListNodee = createListNode(answer)
        return ListNodee
        