class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо посилання на наступний вузол
            current.next = prev       # Перенаправляємо поточний вузол на попередній
            prev = current            # Оновлюємо «попередній» вузол на поточний
            current = next_node       # Переходимо до наступного вузла
        self.head = prev              # новий head - це останній вузол з вихідного списку
