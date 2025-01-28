from b_tree import Node, draw_tree

def build_heap_tree(heap_array):
    nodes = [Node(val) for val in heap_array]  # Створення вузлів для кожного елемента купи

    # Побудова дерева на основі масиву купи
    for i in range(len(heap_array)):
        if 2 * i + 1 < len(heap_array):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(heap_array):
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]  # повернути кореневий вузол

def tree_to_list(root_node):
    result = []
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            result.append(node.val)
            inorder_traversal(node.right)
    inorder_traversal(root_node)

    return result


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    draw_tree(root)

    heap_array = tree_to_list(root)  # Перетворимо дерево на список
    heap_root = build_heap_tree(heap_array)

    draw_tree(heap_root)