class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize the node with a value and a pointer to the next node
        self.val = val
        self.next = next


def array_to_linked_list(arr):
    # Create a dummy node to serve as the starting point of the linked list
    dummy = ListNode()
    current = dummy

    # Iterate through the array and create new nodes
    for value in arr:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head = array_to_linked_list(arr)


def print_linked_list(head):
    # Initialize a pointer to traverse the linked list
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


print_linked_list(head)
