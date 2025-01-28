from collections import deque
from b_tree import lighten_color, rgb_to_hex, hex_to_rgb, draw_tree

def bfs_traversal(root):
    """Обхід дерева завширшки (BFS) з використанням черги."""
    queue = deque([root])
    visited = set()
    step = 0
    total_steps = 10
    base_color = hex_to_rgb(root.color)

    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)

            new_color = lighten_color(base_color, step, total_steps)
            node.color = rgb_to_hex(new_color)
            step += 1
            draw_tree(root, f"BFS Step {step}")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
