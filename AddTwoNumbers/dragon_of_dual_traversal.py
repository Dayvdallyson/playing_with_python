class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linkedList1 = LinkedList(2, LinkedList(4, LinkedList(3)))
linkedList2 = LinkedList(5, LinkedList(6, LinkedList(4)))


def printLinkedList(linkedList1, linkedList2):
    while linkedList1 and linkedList2:
        print(linkedList1.val, linkedList2.val)
        linkedList1 = linkedList1.next
        linkedList2 = linkedList2.next


printLinkedList(linkedList1, linkedList2)
