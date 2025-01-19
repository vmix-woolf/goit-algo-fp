from task01.subtaskA.llist import Node

def insertion_sort(linked_list):
    # Перевіряємо, якщо список порожній або містить один елемент, то сортування не потрібне
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    sorted_dummy = Node()
    current = linked_list.head
    while current:
        # save next node before link changing
        next_node = current.next

        # find insertion place
        prev = sorted_dummy
        while prev.next and prev.next.data < current.data:
            prev = prev.next

        # insertion
        current.next = prev.next
        prev.next = current
        current = next_node

    # update head to the new sorted part
    linked_list.head = sorted_dummy.next

    return linked_list
