class LinkedList:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next



list1 = LinkedList(2, LinkedList(5, LinkedList(7, LinkedList(9))))
list2 = LinkedList(1, LinkedList(3, LinkedList(4, LinkedList(6, LinkedList(8, LinkedList(9))))))


while list1 or list2:
	print(list1.val, list2.val, end=" -> ")
	list1 = list1.next if list1 else None
	list2 = list2.next
