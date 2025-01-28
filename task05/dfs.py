from b_tree import lighten_color, rgb_to_hex, hex_to_rgb, draw_tree

def dfs_traversal(root):
    """Обхід дерева в глибину (DFS) з використанням стека."""
    stack = [root]
    visited = set()
    step = 0
    total_steps = 10  # Загальна кількість кроків для генерації кольорів
    base_color = hex_to_rgb(root.color)  # Початковий колір у RGB

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            # Освітлюємо колір на основі кроку
            new_color = lighten_color(base_color, step, total_steps)
            node.color = rgb_to_hex(new_color)
            step += 1
            draw_tree(root, f"DFS Step {step}")  # Візуалізація поточного стану дерева

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
