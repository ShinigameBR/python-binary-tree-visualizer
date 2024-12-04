from binary_tree import BinaryTree
from plot_tree import plot_tree

# Criando a árvore binária
bt = BinaryTree(1)
bt.create_balanced_tree(100)  # Criar árvore binária balanceada com 100 nós


# Visualizando a árvore binária
plot_tree(bt.root)
