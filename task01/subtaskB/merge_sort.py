from task01.subtaskA.llist import Node, LinkedList

def merge_sort(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    def split_list(head):
        """ For splitting list into two parts """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        return head, middle

    def merge_lists(left, right):
        """ For two sorted lists merging """
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

    left_head, right_head = split_list(linked_list.head)

    # each part sorting recursively
    left_list = LinkedList()
    left_list.head = left_head
    left_sorted = merge_sort(left_list)

    right_list = LinkedList()
    right_list.head = right_head
    right_sorted = merge_sort(right_list)

    sorted_head = merge_lists(left_sorted.head, right_sorted.head)

    # # update head to the new sorted part
    linked_list.head = sorted_head

    return linked_list
