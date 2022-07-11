# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        FinalList = []
        while True:
            try:
                FinalList.append(list1.val)
                list1 = list1.next
            except:
                break
        while True:
            try:
                FinalList.append(list2.val)
                list2 = list2.next
            except:
                break
        FinalList.sort()
        def createListNode(myList):
            if len(myList) == 0:
                return list1
            elif len(myList) == 1:
                return ListNode(myList[0])
            else:
                deneme = ListNode(val=myList[0],next=(createListNode(myList[1:])))
                return deneme
        return createListNode(FinalList)
