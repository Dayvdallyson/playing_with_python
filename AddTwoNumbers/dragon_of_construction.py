class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def array_to_linked_list(values):
	dummy = ListNode()
	current = dummy
	if not values:
		return None

	for val in values:
		current.next = ListNode(val)
		current = current.next
	return dummy.next

array_transformed = array_to_linked_list([7, 0, 8])
current = array_transformed

while current:
	print(current.val, end=" -> ")
	current = current.next
