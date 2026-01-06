class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


linkedList1 = LinkedList(20)
linkedList2 = LinkedList(30)
linkedList3 = LinkedList(40)

linkedList1.next = linkedList2
linkedList2.next = linkedList3

current = linkedList1

while current:
    print(current.val, end=" -> ")
    current = current.next
    if not current:
        break
