from task01.subtaskA.llist import Node, LinkedList
from task01.subtaskB.main import create_linked_list

def merge_lists(left: Node, right: Node):
    dummy = Node()
    tail = dummy

    while left and right:
        if left.data < right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right

    return dummy.next


if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    even_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    left_linked_list = create_linked_list(odd_list)
    left_linked_list.reverse()
    right_linked_list = create_linked_list(even_list)
    right_linked_list.reverse()

    merged_list = LinkedList()
    merged_list.head = merge_lists(left_linked_list.head, right_linked_list.head)
    print("\nSorted list:")
    merged_list.display()