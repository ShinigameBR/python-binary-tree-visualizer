import matplotlib.pyplot as plt
import networkx as nx

# Função para desenhar a árvore binária
def plot_tree(root):
    G = nx.DiGraph()

    def add_edges(node, pos, x=0, y=0, layer=1):
        if node is not None:
            G.add_node(node.value, pos=(x, y))
            if node.left:
                G.add_edge(node.value, node.left.value)
                l = x - 1 / layer
                add_edges(node.left, pos, x=l, y=y-1, layer=layer+1)
            if node.right:
                G.add_edge(node.value, node.right.value)
                r = x + 1 / layer
                add_edges(node.right, pos, x=r, y=y-1, layer=layer+1)

    add_edges(root, {})

    pos = nx.get_node_attributes(G, 'pos')

    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, with_labels=True, arrows=True, node_size=5000, node_color="skyblue", font_size=10, font_weight='bold')
    plt.title("Árvore Binária (1 a 1000)")
    plt.show()
