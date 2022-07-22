class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        FinalList = []
        while True:
            try:
                FinalList.append(head.val)
                head = head.next
            except:
                break
        FinalList.reverse()
        def createListNode(myList):
            if len(myList) == 0:
                return head
            elif len(myList) == 1:
                return ListNode(myList[0])
            else:
                deneme = ListNode(val=myList[0],next=(createListNode(myList[1:])))
                return deneme
        return createListNode(FinalList)