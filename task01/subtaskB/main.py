from task01.subtaskB.insertion_sort import insertion_sort
from task01.subtaskB.merge_sort import merge_sort
from task01.subtaskA.llist import LinkedList

def create_linked_list(values):
    llist = LinkedList()
    for value in values:
        llist.append(value)
    return llist

def print_linked_list(llist: LinkedList):
    llist.display()


if __name__ == '__main__':
    original_list = [4, 2, 1, 3, 5, 10, 7, 9, 8, 6]
    original_llist = create_linked_list(original_list)

    print("Source list:")
    print_linked_list(original_llist)

    sorted_list = insertion_sort(original_llist)
    print("\nInsertion sort:")
    print_linked_list(sorted_list)

    sorted_list = merge_sort(original_llist)
    print("\nMerge sort:")
    print_linked_list(sorted_list)