from llist import LinkedList

def main():
    llist = LinkedList()
    llist.append(5)
    llist.append(15)
    llist.append(25)
    llist.append(35)
    llist.append(45)
    llist.display()
    llist.reverse()
    llist.display()


if __name__ == '__main__':
    main()
