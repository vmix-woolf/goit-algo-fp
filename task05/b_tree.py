import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#17CEEB"):  # Початковий колір skyblue у форматі HEX
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, step_title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(step_title)  # Заголовок для поточного кроку
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def hex_to_rgb(hex_color):
    """Перетворює HEX-колір на RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Перетворює RGB-колір на HEX."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def lighten_color(rgb, step, total_steps):
    """Освітлює колір на основі кроку обходу."""
    r, g, b = rgb
    # Збільшуємо інтенсивність кожного каналу
    r = min(255, r + int((255 - r) * (step / total_steps)))
    g = min(255, g + int((255 - g) * (step / total_steps)))
    b = min(255, b + int((255 - b) * (step / total_steps)))

    return r, g, b
