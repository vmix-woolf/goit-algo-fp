from b_tree import Node
from bfs import bfs_traversal
from dfs import dfs_traversal


if __name__ == '__main__':
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Візуалізація обходу в глибину (DFS)
    print("DFS Traversal:")
    dfs_traversal(root)

    # Візуалізація обходу в ширину (BFS)
    print("BFS Traversal:")
    bfs_traversal(root)
