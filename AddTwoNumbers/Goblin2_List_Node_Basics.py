class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def array_to_linked_list(array):
    if not array:
        return None

    head = Node(array[0])
    current = head

    for value in array[1:]:
        current.next = Node(value)
        current = current.next

    return head


def linked_list_to_array(head):
    result = []
    current = head

    while current:
        result.append(current.value)
        current = current.next

    return result


array_original = [10, 20, 30, 40, 50]

head = array_to_linked_list(array_original)

array_final = linked_list_to_array(head)

while head:
    print(head.value)
    head = head.next
